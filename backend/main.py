
"""
Student/Employee Information Chatbot - FastAPI Backend
Production-ready with JWT auth, RAG, and role-based access
NO OPENAI REQUIRED - Uses open-source alternatives
"""

from fastapi import FastAPI, HTTPException, Depends, status, BackgroundTasks
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import sqlite3
import hashlib
import jwt
import datetime
import json
import re
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from llm_integration import get_llm

# Configuration
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

app = FastAPI(title="Student/Employee Chatbot API")
security = HTTPBearer()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serves the frontend files directly (Combined Server)
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Mount frontend directory
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# Initialize sentence transformer model (runs locally, no API needed)
print("Loading embedding model... (this may take a minute on first run)")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Small, fast, local model
print("Model loaded successfully!")

# FAISS index for vector search
dimension = 384  # Dimension of all-MiniLM-L6-v2 embeddings
faiss_index = faiss.IndexFlatL2(dimension)
document_store = []  # Store documents with their IDs

# Database initialization
def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL,
        linked_id TEXT
    )''')
    
    # Students table
    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        year INTEGER,
        attendance REAL,
        grades TEXT,
        fees_due REAL,
        email TEXT,
        phone TEXT,
        address TEXT,
        gpa REAL
    )''')
    
    # Employees table
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        designation TEXT,
        department TEXT,
        salary REAL,
        leave_balance INTEGER,
        email TEXT,
        phone TEXT,
        hire_date TEXT
    )''')
    
    # FAQ table
    c.execute('''CREATE TABLE IF NOT EXISTS faq (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        category TEXT,
        views INTEGER DEFAULT 0
    )''')
    
    # Policies table
    c.execute('''CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        category TEXT,
        effective_date TEXT
    )''')
    
    # Courses table
    c.execute('''CREATE TABLE IF NOT EXISTS courses (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        instructor_id TEXT,
        credits INTEGER,
        schedule TEXT,
        capacity INTEGER,
        enrolled INTEGER DEFAULT 0,
        description TEXT
    )''')
    
    # Events table
    c.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL,
        time TEXT,
        location TEXT,
        category TEXT,
        organizer TEXT
    )''')
    
    # Announcements table
    c.execute('''CREATE TABLE IF NOT EXISTS announcements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        date TEXT NOT NULL,
        priority TEXT,
        target_audience TEXT,
        author TEXT
    )''')
    
    # Resources table
    c.execute('''CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        type TEXT,
        url TEXT,
        category TEXT,
        tags TEXT
    )''')
    
    # Chat history table
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        message TEXT NOT NULL,
        response TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        sentiment TEXT,
        intent TEXT
    )''')
    
    # Conversation context table
    c.execute('''CREATE TABLE IF NOT EXISTS conversation_context (
        user_id TEXT PRIMARY KEY,
        last_topic TEXT,
        last_intent TEXT,
        context_data TEXT,
        last_updated TEXT
    )''')
    
    conn.commit()
    conn.close()

# Pydantic models
class LoginRequest(BaseModel):
    user_id: str
    password: str

class ChatRequest(BaseModel):
    message: str

class UserCreate(BaseModel):
    user_id: str
    password: str
    role: str
    linked_id: Optional[str] = None

class StudentCreate(BaseModel):
    id: str
    name: str
    department: str
    year: int
    attendance: float
    grades: str
    fees_due: float
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    gpa: Optional[float] = None

class EmployeeCreate(BaseModel):
    id: str
    name: str
    designation: str
    department: str
    salary: float
    leave_balance: int
    email: str
    phone: Optional[str] = None
    hire_date: Optional[str] = None

class FAQCreate(BaseModel):
    question: str
    answer: str
    category: Optional[str] = "General"

class PolicyCreate(BaseModel):
    title: str
    content: str
    category: Optional[str] = "General"
    effective_date: Optional[str] = None

class CourseCreate(BaseModel):
    id: str
    name: str
    department: str
    instructor_id: Optional[str] = None
    credits: int
    schedule: str
    capacity: int
    description: Optional[str] = None

class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    date: str
    time: Optional[str] = None
    location: Optional[str] = None
    category: Optional[str] = "General"
    organizer: Optional[str] = None

class AnnouncementCreate(BaseModel):
    title: str
    content: str
    priority: Optional[str] = "normal"
    target_audience: Optional[str] = "all"

class ResourceCreate(BaseModel):
    title: str
    description: Optional[str] = None
    type: str
    url: Optional[str] = None
    category: Optional[str] = "General"
    tags: Optional[str] = None

# Helper functions
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_db():
    conn = sqlite3.connect('chatbot.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_user_data(user_id: str, role: str, linked_id: str):
    """Fetch user's personal data based on role"""
    conn = get_db()
    c = conn.cursor()
    
    data = {}
    if role == "student":
        c.execute("SELECT * FROM students WHERE id = ?", (linked_id,))
        row = c.fetchone()
        if row:
            data = dict(row)
    elif role == "employee":
        c.execute("SELECT * FROM employees WHERE id = ?", (linked_id,))
        row = c.fetchone()
        if row:
            data = dict(row)
    elif role == "admin":
        # Admin can see summary data
        c.execute("SELECT COUNT(*) as count FROM students")
        student_count = c.fetchone()[0]
        c.execute("SELECT COUNT(*) as count FROM employees")
        employee_count = c.fetchone()[0]
        data = {
            'role': 'admin',
            'total_students': student_count,
            'total_employees': employee_count,
            'message': 'Full admin access granted'
        }
    
    conn.close()
    return data

def add_to_vector_db(text: str, doc_id: str):
    """Add document to FAISS vector database"""
    global faiss_index, document_store
    
    # Generate embedding
    embedding = embedding_model.encode([text])[0]
    
    # Add to FAISS
    faiss_index.add(np.array([embedding], dtype=np.float32))
    
    # Store document
    document_store.append({"id": doc_id, "text": text})

def search_knowledge_base(query: str, n_results: int = 3) -> List[str]:
    """Search vector database for relevant documents"""
    global faiss_index, document_store
    
    if len(document_store) == 0:
        return []
    
    try:
        # Generate query embedding
        query_embedding = embedding_model.encode([query])[0]
        
        # Search FAISS
        distances, indices = faiss_index.search(
            np.array([query_embedding], dtype=np.float32), 
            min(n_results, len(document_store))
        )
        
        # Get relevant documents
        results = []
        for idx in indices[0]:
            if idx < len(document_store):
                results.append(document_store[idx]['text'])
        
        return results
    except Exception as e:
        print(f"Search error: {e}")
        return []

def detect_intent(query: str) -> str:
    """Detect user's intent from query"""
    query_lower = query.lower()
    
    # Personal info intents
    if any(word in query_lower for word in ["attendance", "attend", "present"]):
        return "check_attendance"
    if any(word in query_lower for word in ["grade", "marks", "score", "result", "gpa"]):
        return "check_grades"
    if any(word in query_lower for word in ["fee", "fees", "payment", "due", "owe"]):
        return "check_fees"
    if any(word in query_lower for word in ["leave", "vacation", "days off", "holiday"]):
        return "check_leave"
    if any(word in query_lower for word in ["salary", "pay", "wage", "compensation"]):
        return "check_salary"
    if any(word in query_lower for word in ["profile", "info", "information", "details", "about me"]):
        return "view_profile"
    
    # Course intents
    if any(word in query_lower for word in ["course", "class", "subject"]) and any(word in query_lower for word in ["list", "what", "show", "all"]):
        return "list_courses"
    if any(word in query_lower for word in ["enroll", "register", "join"]):
        return "enroll_course"
    if any(word in query_lower for word in ["schedule", "timetable"]):
        return "view_schedule"
    
    # Event intents
    if any(word in query_lower for word in ["event", "events"]):
        return "list_events"
    
    # Announcement intents
    if any(word in query_lower for word in ["announcement", "news", "update"]):
        return "list_announcements"
    
    # Search intent
    if any(word in query_lower for word in ["search", "find", "look for", "where can i"]):
        return "search"
    
    # Greeting intent
    if any(word in query_lower for word in ["hello", "hi", "hey", "greetings"]):
        return "greeting"
    
    # Help intent
    if any(word in query_lower for word in ["help", "support", "assist", "what can you"]):
        return "help"
    
    # Thanks intent
    if any(word in query_lower for word in ["thank", "thanks"]):
        return "thanks"
    
    return "general_query"

def analyze_sentiment(text: str) -> str:
    """Simple sentiment analysis based on keywords"""
    text_lower = text.lower()
    
    positive_words = ["great", "excellent", "good", "thanks", "thank you", "awesome", "wonderful", "perfect", "love", "happy"]
    negative_words = ["bad", "poor", "terrible", "worst", "hate", "angry", "frustrated", "disappointed", "confused", "problem"]
    
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"

def get_conversation_context(user_id: str) -> Dict:
    """Get user's conversation context"""
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM conversation_context WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    
    if row:
        return {
            'last_topic': row['last_topic'],
            'last_intent': row['last_intent'],
            'context_data': json.loads(row['context_data']) if row['context_data'] else {}
        }
    return {'last_topic': None, 'last_intent': None, 'context_data': {}}

def update_conversation_context(user_id: str, topic: str, intent: str, context_data: Dict = None):
    """Update user's conversation context"""
    conn = get_db()
    c = conn.cursor()
    
    context_json = json.dumps(context_data) if context_data else '{}'
    timestamp = datetime.datetime.now().isoformat()
    
    c.execute('''INSERT OR REPLACE INTO conversation_context 
                 (user_id, last_topic, last_intent, context_data, last_updated) 
                 VALUES (?, ?, ?, ?, ?)''',
              (user_id, topic, intent, context_json, timestamp))
    conn.commit()
    conn.close()

def save_chat_history(user_id: str, message: str, response: str, sentiment: str, intent: str):
    """Save chat interaction to history"""
    conn = get_db()
    c = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    
    c.execute('''INSERT INTO chat_history 
                 (user_id, message, response, timestamp, sentiment, intent) 
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (user_id, message, response, timestamp, sentiment, intent))
    conn.commit()
    conn.close()

def generate_rule_based_response(user_query: str, user_data: dict, context_docs: List[str], role: str, context: Dict = None) -> str:
    """Generate response using rule-based AI with context awareness"""
    
    query_lower = user_query.lower()
    intent = detect_intent(user_query)
    
    # Handle context-aware follow-up questions
    if context and context.get('last_intent'):
        if any(word in query_lower for word in ["more", "details", "tell me more", "elaborate"]):
            return "I'd be happy to provide more information! Could you please specify what aspect you'd like to know more about?"
    
    # Personal data queries
    if role == "student" and user_data:
        if intent == "check_attendance":
            attendance = user_data.get('attendance', 'N/A')
            if attendance != 'N/A' and attendance >= 75:
                return f"✅ Your current attendance is {attendance}%. Great job! You're meeting the minimum 75% requirement. Keep it up!"
            elif attendance != 'N/A':
                return f"⚠️ Your current attendance is {attendance}%. You need to maintain at least 75% attendance to be eligible for final exams. Please improve your attendance."
            return f"Your current attendance is {attendance}%."
        
        if intent == "check_grades":
            grades = user_data.get('grades', 'N/A')
            gpa = user_data.get('gpa', 'N/A')
            response = f"📊 Your current grade is {grades}."
            if gpa != 'N/A':
                response += f" Your GPA is {gpa}."
            response += "\n\nGrades are based on:\n• Assignments: 20%\n• Mid-terms: 30%\n• Finals: 40%\n• Participation: 10%"
            return response
        
        if intent == "check_fees":
            fees = user_data.get('fees_due', 0)
            if fees == 0:
                return "✅ Great news! You have no pending fees. Your account is fully paid."
            else:
                return f"💰 You currently have ${fees:.2f} in pending fees.\n\nPayment options:\n• Online through the student portal\n• In-person at Finance Office (Building C)\n• Bank transfer (details in portal)"
        
        if intent == "view_profile":
            name = user_data.get('name', 'Student')
            dept = user_data.get('department', 'N/A')
            year = user_data.get('year', 'N/A')
            phone = user_data.get('phone', 'N/A')
            response = f"👤 **Your Profile**\n\n"
            response += f"**Name:** {name}\n"
            response += f"**Department:** {dept}\n"
            response += f"**Year:** {year}\n"
            response += f"**Email:** {user_data.get('email', 'N/A')}\n"
            response += f"**Phone:** {phone}\n"
            response += f"**Attendance:** {user_data.get('attendance', 'N/A')}%\n"
            response += f"**Grades:** {user_data.get('grades', 'N/A')}"
            if user_data.get('gpa'):
                response += f"\n**GPA:** {user_data.get('gpa')}"
            return response
    
    elif role == "employee" and user_data:
        if intent == "check_leave":
            leave = user_data.get('leave_balance', 0)
            response = f"🏖️ You have **{leave} days** of paid leave remaining.\n\n"
            response += "**Leave Policy:**\n"
            response += "• Submit requests through HR portal\n"
            response += "• Approval needed 1 week in advance\n"
            response += "• Maximum 10 consecutive days\n"
            response += "• Annual leave: 20 days"
            return response
        
        if intent == "check_salary":
            salary = user_data.get('salary', 0)
            response = f"💵 Your annual salary is **${salary:,.2f}**\n\n"
            response += "**Payment Schedule:**\n"
            response += "• Paid monthly on the last working day\n"
            response += "• Direct deposit to registered bank account\n"
            response += "• Pay slips available in HR portal"
            return response
        
        if intent == "view_profile":
            name = user_data.get('name', 'Employee')
            designation = user_data.get('designation', 'N/A')
            dept = user_data.get('department', 'N/A')
            response = f"👤 **Your Profile**\n\n"
            response += f"**Name:** {name}\n"
            response += f"**Designation:** {designation}\n"
            response += f"**Department:** {dept}\n"
            response += f"**Email:** {user_data.get('email', 'N/A')}\n"
            response += f"**Phone:** {user_data.get('phone', 'N/A')}\n"
            response += f"**Hire Date:** {user_data.get('hire_date', 'N/A')}\n"
            response += f"**Leave Balance:** {user_data.get('leave_balance', 'N/A')} days"
            return response
    
    elif role == "admin":
        if any(word in query_lower for word in ["student", "students"]):
            return f"📊 **System Overview - Students**\n\nTotal Students: {user_data.get('total_students', 0)}\n\nYou have full administrative access to view and manage all student records through the admin panel."
        if any(word in query_lower for word in ["employee", "employees", "staff"]):
            return f"📊 **System Overview - Employees**\n\nTotal Employees: {user_data.get('total_employees', 0)}\n\nYou have full administrative access to view and manage all employee records through the admin panel."
    
    # Intent-based responses
    if intent == "greeting":
        responses = [
            f"Hello! 👋 I'm your university assistant. How can I help you today?",
            f"Hi there! 😊 I'm here to assist you. What would you like to know?",
            f"Greetings! I can help you with information about your records, courses, events, and more. What do you need?"
        ]
        import random
        return random.choice(responses)
    
    if intent == "thanks":
        responses = [
            "You're very welcome! Feel free to ask if you need anything else. 😊",
            "Happy to help! Don't hesitate to reach out if you have more questions.",
            "You're welcome! I'm here whenever you need assistance."
        ]
        import random
        return random.choice(responses)
    
    if intent == "help":
        response = "🤖 **I can help you with:**\n\n"
        response += "📝 **Personal Information:**\n• View your profile\n• Check attendance/leave\n• View grades/salary\n• Check fees/payments\n\n"
        response += "📚 **Academic:**\n• List courses\n• View schedule\n• Academic policies\n\n"
        response += "📅 **Campus Life:**\n• Upcoming events\n• Announcements\n• Campus facilities\n\n"
        response += "❓ **Resources:**\n• FAQs\n• Policies\n• Contact information\n\n"
        response += "Just ask me a question in natural language!"
        return response
    
    # Knowledge base queries
    if context_docs:
        response = "📚 **Here's what I found:**\n\n"
        for i, doc in enumerate(context_docs[:2], 1):
            response += f"{doc}\n\n"
        return response.strip()
    
    # General facility queries
    if any(word in query_lower for word in ["library", "hours"]):
        return "📖 **Library Information:**\n\n**Hours:**\n• Monday-Friday: 8:00 AM - 10:00 PM\n• Saturday: 10:00 AM - 6:00 PM\n• Sunday: 12:00 PM - 8:00 PM\n\n**Services:**\n• Study rooms (bookable online)\n• Computer lab\n• Printing services\n• Research assistance"
    
    if any(word in query_lower for word in ["cafeteria", "food", "dining", "eat", "lunch", "breakfast"]):
        return "🍽️ **Dining Services:**\n\n**Main Cafeteria** (Building B, Ground Floor)\n• Breakfast: 7:00-9:00 AM\n• Lunch: 12:00-2:00 PM\n• Dinner: 6:00-8:00 PM\n\n**Food Court** (Student Center)\n• Open: 10:00 AM - 8:00 PM\n• Various cuisines available"
    
    if any(word in query_lower for word in ["support", "contact", "help desk"]):
        return "📞 **Support & Contact:**\n\n**IT Support:**\n• Location: Building A, Room 101\n• Email: support@university.edu\n• Phone: (555) 123-4567\n\n**Academic Support:**\n• Contact your academic advisor\n• Email: advising@university.edu\n\n**Administrative:**\n• Main Office: Building C\n• Email: admin@university.edu"
    
    # Default helpful response
    return f"I understand you're asking about '{user_query}'. While I can provide general assistance, I'd like to help you more specifically.\n\nI can assist with:\n• Your personal records and information\n• Course information and schedules\n• University policies and procedures\n• Campus facilities and services\n• Upcoming events and announcements\n\nCould you please rephrase your question or ask something more specific?"

# API Routes
@app.on_event("startup")
async def startup_event():
    init_db()
    try:
        initialize_sample_data()
    except Exception as e:
        print(f"Data init skipped or failed: {e}")

    # Create a guaranteed faculty user - COMMENTED OUT TO PREVENT CRASH
    # conn = sqlite3.connect('chatbot.db')
    # c = conn.cursor()
    # # Faculty ID: FAC101, Password: FAC101
    # fac_pw_hash = hashlib.sha256("FAC101".encode()).hexdigest()
    # 
    # # Check if exists first
    # c.execute("SELECT * FROM users WHERE user_id = 'FAC101'")
    # if not c.fetchone():
    #     print("Creating demo faculty account: FAC101")
    #     c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", ("FAC101", fac_pw_hash, "employee", "FAC101"))
    #     c.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #              ("FAC101", "Dr. Sarah Smith", "Professor", "Computer Science", 95000.0, 15, "sarah@hicas.ac.in", "+91 9876543210", "2020-01-15"))
    #     conn.commit()
    # conn.close()

@app.post("/login")
async def login(request: LoginRequest):
    """Authenticate user and return JWT token"""
    print(f"DEBUG LOGIN Attempt: User={request.user_id}, Password={request.password}") # DEBUG LOG
    
    conn = get_db()
    c = conn.cursor()
    
    password_hash = hash_password(request.password)
    print(f"DEBUG Hash: {password_hash}") # DEBUG LOG
    
    # Check if user exists at all first
    c.execute("SELECT * FROM users WHERE user_id = ?", (request.user_id,))
    user_exists = c.fetchone()
    if not user_exists:
        print(f"DEBUG: User '{request.user_id}' NOT FOUND in users table")
    else:
        print(f"DEBUG: User found. Role: {user_exists['role']}, Stored Hash: {user_exists['password_hash']}")
    
    # Check full credentials
    c.execute("SELECT * FROM users WHERE user_id = ? AND password_hash = ?",
              (request.user_id, password_hash))
    user = c.fetchone()
    conn.close()
    
    if not user:
        print("DEBUG: Login FAILED - Hash mismatch or user not found")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    print("DEBUG: Login SUCCESS")
    
    token_data = {
        "user_id": user['user_id'],
        "role": user['role'],
        "linked_id": user['linked_id']
    }
    token = create_access_token(token_data)
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user['role']
    }

@app.post("/register")
async def register(user: UserCreate):
    """Register a new user"""
    conn = get_db()
    c = conn.cursor()
    
    # Check if user already exists
    c.execute("SELECT * FROM users WHERE user_id = ?", (user.user_id,))
    if c.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="User already exists")
    
    password_hash = hash_password(user.password)
    
    # Insert new user
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
              (user.user_id, password_hash, user.role, user.linked_id if user.linked_id else user.user_id))
    
    # If student/employee, create basic record if not exists
    if user.role == "student":
        c.execute("INSERT OR IGNORE INTO students (id, name, department, year, attendance, grades, fees_due) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (user.user_id, "New Student", "General", 1, 0.0, "N/A", 0.0))
    elif user.role == "employee":
        c.execute("INSERT OR IGNORE INTO employees (id, name, designation, department, salary, leave_balance) VALUES (?, ?, ?, ?, ?, ?)",
                 (user.user_id, "New Employee", "Staff", "General", 0.0, 0))
                 
    conn.commit()
    conn.close()
    
    return {"message": "User registered successfully"}

    # Personal data queries
    # ... (existing code for rule-based responses) ...

def get_dynamic_context(role: str) -> Dict:
    """Generate random but appropriate context for schedules/events"""
    import random
    from datetime import datetime, timedelta
    
    now = datetime.now()
    
    # Common holidays
    holidays = [
        "Republic Day (Jan 26)", "Independence Day (Aug 15)", 
        "Gandhi Jayanti (Oct 2)", "Deepavali (Nov 12)", 
        "Christmas (Dec 25)", "Pongal (Jan 15)"
    ]
    next_holiday = random.choice(holidays)
    
    context = {
        "current_time": now.strftime("%I:%M %p"),
        "current_date": now.strftime("%Y-%m-%d"),
        "next_holiday": next_holiday
    }
    
    if role == "student":
        subjects = ["Data Structures", "Computer Networks", "Operating Systems", "AI & ML", "Web Development"]
        context["next_class"] = random.choice(subjects)
        context["next_exam"] = f"{random.choice(subjects)} Mid-term"
        context["exam_date"] = (now + timedelta(days=random.randint(10, 30))).strftime("%Y-%m-%d")
        context["next_hour_activity"] = f"Attend {random.choice(subjects)} Lecture"
        
    elif role == "employee":
        tasks = ["Faculty Meeting", "Research Review", "Department Sync", "Proctoring Duty"]
        classes = ["CS101 Lecture", "CS202 Lab", "Final Year Project Review"]
        context["next_task"] = random.choice(tasks)
        context["next_class_to_teach"] = random.choice(classes)
        context["next_hour_activity"] = f"Conduct {random.choice(classes)}"
        context["submission_deadline"] = "Grades submission due next Friday"
        
    return context

@app.post("/chat")
async def chat(request: ChatRequest, user_data: dict = Depends(verify_token)):
    """Process chat message with RAG and context awareness"""
    
    # Get conversation context
    context = get_conversation_context(user_data['user_id'])
    
    # Get user's personal data
    personal_data = get_user_data(
        user_data['user_id'],
        user_data['role'],
        user_data.get('linked_id')
    )
    
    # Get dynamic/random context (schedule, holidays, etc.)
    dynamic_context = get_dynamic_context(user_data['role'])
    
    # Merge personal data with dynamic context for LLM
    full_user_context = {**personal_data, **dynamic_context}
    
    # Search knowledge base
    relevant_docs = search_knowledge_base(request.message)
    
    # Detect intent and sentiment
    intent = detect_intent(request.message)
    sentiment = analyze_sentiment(request.message)
    
    # Generate response using LOCAL LLM (Phi-3 Mini)
    llm = get_llm()
    response = llm.generate_response(
        user_query=request.message,
        user_data=full_user_context,  # Passed combined data
        context_docs=relevant_docs,
        role=user_data['role'],
        conversation_history=None
    )
    
    # Update conversation context
    update_conversation_context(
        user_data['user_id'],
        topic=request.message[:50],  # Store first 50 chars as topic
        intent=intent,
        context_data={'last_query': request.message}
    )
    
    # Save to chat history
    save_chat_history(
        user_data['user_id'],
        request.message,
        response,
        sentiment,
        intent
    )
    
    return {
        "response": response,
        "timestamp": datetime.datetime.now().isoformat(),
        "intent": intent,
        "sentiment": sentiment
    }

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest, background_tasks: BackgroundTasks, user_data: dict = Depends(verify_token)):
    """Stream chat response for better UX"""
    
    # Context and Data
    context = get_conversation_context(user_data['user_id'])
    personal_data = get_user_data(user_data['user_id'], user_data['role'], user_data.get('linked_id'))
    relevant_docs = search_knowledge_base(request.message)
    intent = detect_intent(request.message)
    sentiment = analyze_sentiment(request.message)
    
    llm = get_llm()
    
    # Store complete response for history
    full_response = []
    
    async def response_generator():
        # Yield metadata first (optional, or just stream text)
        # We'll just stream text for simplicity in this version
        
        if llm.available:
            # Stream from LLM
            stream = llm.stream_response(
                user_query=request.message,
                user_data=personal_data,
                context_docs=relevant_docs,
                role=user_data['role']
            )
            
            for chunk in stream:
                full_response.append(chunk)
                yield chunk
        else:
            # Fallback (simulate stream)
            response = generate_rule_based_response(
                request.message, personal_data, relevant_docs, user_data['role'], context
            )
            full_response.append(response)
            yield response
            
        # After streaming is done, save history (this runs in the generator context)
        # To be safe, we use background tasks passed to the endpoint, but we need
        # to trigger it. Actually, BackgroundTasks run *after* the response.
        # But since we are streaming, we can't easily use standard BackgroundTasks for
        # the accumulated content unless we pass a mutable object or do it here.
        
        # We'll save it right here at the end of the stream
        save_chat_history(
            user_data['user_id'],
            request.message,
            "".join(full_response),
            sentiment,
            intent
        )
        
        update_conversation_context(
            user_data['user_id'],
            topic=request.message[:50],
            intent=intent,
            context_data={'last_query': request.message}
        )

    return StreamingResponse(response_generator(), media_type="text/plain")

@app.get("/me")
async def get_profile(user_data: dict = Depends(verify_token)):
    """Get current user's profile"""
    return {
        "user_id": user_data['user_id'],
        "role": user_data['role'],
        "linked_id": user_data.get('linked_id')
    }

@app.get("/my-records")
async def get_my_records(user_data: dict = Depends(verify_token)):
    """Get user's personal records"""
    data = get_user_data(
        user_data['user_id'],
        user_data['role'],
        user_data.get('linked_id')
    )
    return data

@app.post("/admin/add-user")
async def add_user(user: UserCreate, current_user: dict = Depends(verify_token)):
    """Admin only: Add new user"""
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required")
    
    conn = get_db()
    c = conn.cursor()
    
    password_hash = hash_password(user.password)
    try:
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                  (user.user_id, password_hash, user.role, user.linked_id))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="User already exists")
    
    conn.close()
    return {"message": "User created successfully"}

@app.post("/admin/add-faq")
async def add_faq(faq: FAQCreate, current_user: dict = Depends(verify_token)):
    """Admin only: Add FAQ and index in vector DB"""
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required")
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute("INSERT INTO faq (question, answer) VALUES (?, ?)",
              (faq.question, faq.answer))
    faq_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Add to vector database
    doc_text = f"Q: {faq.question}\nA: {faq.answer}"
    add_to_vector_db(doc_text, f"faq_{faq_id}")
    
    return {"message": "FAQ added successfully", "id": faq_id}

@app.post("/admin/add-policy")
async def add_policy(policy: PolicyCreate, current_user: dict = Depends(verify_token)):
    """Admin only: Add policy and index in vector DB"""
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required")
    
    conn = get_db()
    c = conn.cursor()
    
    effective_date = policy.effective_date or datetime.datetime.now().strftime("%Y-%m-%d")
    c.execute("INSERT INTO policies (title, content, category, effective_date) VALUES (?, ?, ?, ?)",
              (policy.title, policy.content, policy.category, effective_date))
    policy_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Add to vector database
    doc_text = f"Policy: {policy.title}\nCategory: {policy.category}\n{policy.content}"
    add_to_vector_db(doc_text, f"policy_{policy_id}")
    
    return {"message": "Policy added successfully", "id": policy_id}

@app.get("/courses")
async def get_courses(department: Optional[str] = None, user_data: dict = Depends(verify_token)):
    """Get list of courses, optionally filtered by department"""
    conn = get_db()
    c = conn.cursor()
    
    if department:
        c.execute("SELECT * FROM courses WHERE department = ?", (department,))
    else:
        c.execute("SELECT * FROM courses")
    
    courses = [dict(row) for row in c.fetchall()]
    conn.close()
    return {"courses": courses}

@app.post("/admin/add-course")
async def add_course(course: CourseCreate, current_user: dict = Depends(verify_token)):
    """Admin only: Add new course"""
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required")
    
    conn = get_db()
    c = conn.cursor()
    
    try:
        c.execute('''INSERT INTO courses 
                     (id, name, department, instructor_id, credits, schedule, capacity, description) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (course.id, course.name, course.department, course.instructor_id,
                   course.credits, course.schedule, course.capacity, course.description))
        conn.commit()
        
        # Add to vector DB
        doc_text = f"Course: {course.name} ({course.id})\nDepartment: {course.department}\nCredits: {course.credits}\nSchedule: {course.schedule}\n{course.description or ''}"
        add_to_vector_db(doc_text, f"course_{course.id}")
        
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Course already exists")
    
    conn.close()
    return {"message": "Course added successfully"}

@app.get("/events")
async def get_events(category: Optional[str] = None, upcoming: bool = True, user_data: dict = Depends(verify_token)):
    """Get list of events"""
    conn = get_db()
    c = conn.cursor()
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    if category:
        if upcoming:
            c.execute("SELECT * FROM events WHERE category = ? AND date >= ? ORDER BY date", (category, today))
        else:
            c.execute("SELECT * FROM events WHERE category = ? ORDER BY date DESC", (category,))
    else:
        if upcoming:
            c.execute("SELECT * FROM events WHERE date >= ? ORDER BY date", (today,))
        else:
            c.execute("SELECT * FROM events ORDER BY date DESC")
    
    events = [dict(row) for row in c.fetchall()]
    conn.close()
    return {"events": events}

@app.post("/admin/add-event")
async def add_event(event: EventCreate, current_user: dict = Depends(verify_token)):
    """Admin only: Add new event"""
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required")
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''INSERT INTO events 
                 (title, description, date, time, location, category, organizer) 
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (event.title, event.description, event.date, event.time,
               event.location, event.category, event.organizer))
    event_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Add to vector DB
    doc_text = f"Event: {event.title}\nDate: {event.date} {event.time or ''}\nLocation: {event.location or 'TBA'}\n{event.description or ''}"
    add_to_vector_db(doc_text, f"event_{event_id}")
    
    return {"message": "Event added successfully", "id": event_id}

@app.get("/announcements")
async def get_announcements(priority: Optional[str] = None, limit: int = 10, user_data: dict = Depends(verify_token)):
    """Get recent announcements"""
    conn = get_db()
    c = conn.cursor()
    
    if priority:
        c.execute("SELECT * FROM announcements WHERE priority = ? ORDER BY date DESC LIMIT ?", (priority, limit))
    else:
        c.execute("SELECT * FROM announcements ORDER BY date DESC LIMIT ?", (limit,))
    
    announcements = [dict(row) for row in c.fetchall()]
    conn.close()
    return {"announcements": announcements}

@app.post("/admin/add-announcement")
async def add_announcement(announcement: AnnouncementCreate, current_user: dict = Depends(verify_token)):
    """Admin only: Add new announcement"""
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required")
    
    conn = get_db()
    c = conn.cursor()
    
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    author = current_user['user_id']
    
    c.execute('''INSERT INTO announcements 
                 (title, content, date, priority, target_audience, author) 
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (announcement.title, announcement.content, date,
               announcement.priority, announcement.target_audience, author))
    announcement_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Add to vector DB
    doc_text = f"Announcement: {announcement.title}\nDate: {date}\n{announcement.content}"
    add_to_vector_db(doc_text, f"announcement_{announcement_id}")
    
    return {"message": "Announcement added successfully", "id": announcement_id}

@app.get("/resources")
async def get_resources(category: Optional[str] = None, resource_type: Optional[str] = None, user_data: dict = Depends(verify_token)):
    """Get list of resources"""
    conn = get_db()
    c = conn.cursor()
    
    query = "SELECT * FROM resources WHERE 1=1"
    params = []
    
    if category:
        query += " AND category = ?"
        params.append(category)
    if resource_type:
        query += " AND type = ?"
        params.append(resource_type)
    
    c.execute(query, params)
    resources = [dict(row) for row in c.fetchall()]
    conn.close()
    return {"resources": resources}

@app.post("/admin/add-resource")
async def add_resource(resource: ResourceCreate, current_user: dict = Depends(verify_token)):
    """Admin only: Add new resource"""
    if current_user['role'] != 'admin':
        raise HTTPException(status_code=403, detail="Admin access required")
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''INSERT INTO resources 
                 (title, description, type, url, category, tags) 
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (resource.title, resource.description, resource.type,
               resource.url, resource.category, resource.tags))
    resource_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Add to vector DB
    doc_text = f"Resource: {resource.title}\nType: {resource.type}\nCategory: {resource.category}\n{resource.description or ''}"
    add_to_vector_db(doc_text, f"resource_{resource_id}")
    
    return {"message": "Resource added successfully", "id": resource_id}

@app.get("/chat-history")
async def get_chat_history(limit: int = 20, user_data: dict = Depends(verify_token)):
    """Get user's chat history"""
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''SELECT message, response, timestamp, sentiment, intent 
                 FROM chat_history 
                 WHERE user_id = ? 
                 ORDER BY timestamp DESC 
                 LIMIT ?''', (user_data['user_id'], limit))
    
    history = [dict(row) for row in c.fetchall()]
    conn.close()
    return {"history": history}

@app.get("/search")
async def search(q: str, category: Optional[str] = None, user_data: dict = Depends(verify_token)):
    """Universal search across all content"""
    results = {
        "query": q,
        "results": []
    }
    
    # Search using vector database
    relevant_docs = search_knowledge_base(q, n_results=5)
    
    conn = get_db()
    c = conn.cursor()
    
    # Search FAQs
    c.execute("SELECT question, answer FROM faq WHERE question LIKE ? OR answer LIKE ?", 
              (f"%{q}%", f"%{q}%"))
    faqs = [{"type": "faq", "data": dict(row)} for row in c.fetchall()]
    
    # Search courses
    c.execute("SELECT * FROM courses WHERE name LIKE ? OR description LIKE ?", 
              (f"%{q}%", f"%{q}%"))
    courses = [{"type": "course", "data": dict(row)} for row in c.fetchall()]
    
    # Search events
    c.execute("SELECT * FROM events WHERE title LIKE ? OR description LIKE ?", 
              (f"%{q}%", f"%{q}%"))
    events = [{"type": "event", "data": dict(row)} for row in c.fetchall()]
    
    conn.close()
    
    results["results"] = faqs + courses + events
    results["vector_results"] = relevant_docs
    
    return results

@app.get("/analytics")
async def get_analytics(current_user: dict = Depends(verify_token)):
    """Get analytics dashboard data (admin or personal)"""
    conn = get_db()
    c = conn.cursor()
    
    if current_user['role'] == 'admin':
        # Admin analytics
        c.execute("SELECT COUNT(*) FROM students")
        total_students = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM employees")
        total_employees = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM courses")
        total_courses = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM events WHERE date >= ?", 
                  (datetime.datetime.now().strftime("%Y-%m-%d"),))
        upcoming_events = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM chat_history")
        total_chats = c.fetchone()[0]
        
        c.execute("SELECT sentiment, COUNT(*) as count FROM chat_history GROUP BY sentiment")
        sentiment_stats = [{"sentiment": row[0], "count": row[1]} for row in c.fetchall()]
        
        c.execute("SELECT intent, COUNT(*) as count FROM chat_history GROUP BY intent ORDER BY count DESC LIMIT 10")
        popular_intents = [{"intent": row[0], "count": row[1]} for row in c.fetchall()]
        
        conn.close()
        
        return {
            "total_students": total_students,
            "total_employees": total_employees,
            "total_courses": total_courses,
            "upcoming_events": upcoming_events,
            "total_chats": total_chats,
            "sentiment_distribution": sentiment_stats,
            "popular_intents": popular_intents
        }
    else:
        # Personal analytics
        c.execute("SELECT COUNT(*) FROM chat_history WHERE user_id = ?", (current_user['user_id'],))
        my_chats = c.fetchone()[0]
        
        c.execute("""SELECT sentiment, COUNT(*) as count 
                     FROM chat_history 
                     WHERE user_id = ? 
                     GROUP BY sentiment""", (current_user['user_id'],))
        my_sentiment = [{"sentiment": row[0], "count": row[1]} for row in c.fetchall()]
        
        conn.close()
        
        return {
            "total_chats": my_chats,
            "sentiment_distribution": my_sentiment
        }

def initialize_sample_data():
    """Initialize database with expanded sample data"""
    conn = get_db()
    c = conn.cursor()
    
    # Check if data already exists
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] > 0:
        conn.close()
        return
    
    print("Initializing sample data...")
    
    # Sample students with extended data
    students = [
        ('S001', 'Alice Johnson', 'Computer Science', 2, 92.5, 'A+', 0, 'alice@university.edu', '+1-555-0101', '123 Campus St', 3.9),
        ('S002', 'Bob Smith', 'Electrical Engineering', 3, 85.0, 'B+', 500, 'bob@university.edu', '+1-555-0102', '456 College Ave', 3.5),
        ('S003', 'Carol White', 'Mechanical Engineering', 1, 78.5, 'B', 1000, 'carol@university.edu', '+1-555-0103', '789 University Blvd', 3.2),
        ('S004', 'David Brown', 'Computer Science', 4, 95.0, 'A+', 0, 'david@university.edu', '+1-555-0104', '321 Student Dr', 4.0),
        ('S005', 'Emma Davis', 'Civil Engineering', 2, 88.0, 'A', 250, 'emma@university.edu', '+1-555-0105', '654 Academy Ln', 3.7),
        ('S006', 'Frank Miller', 'Computer Science', 3, 82.0, 'B+', 0, 'frank@university.edu', '+1-555-0106', '987 Scholar Way', 3.4),
        ('S007', 'Grace Lee', 'Electrical Engineering', 1, 90.5, 'A', 0, 'grace@university.edu', '+1-555-0107', '147 Learning St', 3.8),
        ('S008', 'Henry Wilson', 'Mechanical Engineering', 4, 76.0, 'B', 1500, 'henry@university.edu', '+1-555-0108', '258 Education Rd', 3.0),
    ]
    
    c.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", students)
    
    # Sample employees with extended data
    employees = [
        ('E001', 'Prof. John Doe', 'Professor', 'Computer Science', 85000, 15, 'john@university.edu', '+1-555-1001', '2020-01-15'),
        ('E002', 'Dr. Jane Smith', 'Associate Professor', 'Electrical Engineering', 75000, 20, 'jane@university.edu', '+1-555-1002', '2018-08-20'),
        ('E003', 'Mr. Mike Wilson', 'Lab Technician', 'Mechanical Engineering', 45000, 12, 'mike@university.edu', '+1-555-1003', '2021-03-10'),
        ('E004', 'Ms. Sarah Lee', 'Administrator', 'Administration', 55000, 18, 'sarah@university.edu', '+1-555-1004', '2019-06-01'),
        ('E005', 'Dr. Robert Taylor', 'Dean', 'Engineering', 95000, 10, 'robert@university.edu', '+1-555-1005', '2015-09-01'),
        ('E006', 'Prof. Maria Garcia', 'Professor', 'Civil Engineering', 82000, 14, 'maria@university.edu', '+1-555-1006', '2017-01-15'),
        ('E007', 'Dr. James Anderson', 'Department Head', 'Computer Science', 90000, 16, 'james@university.edu', '+1-555-1007', '2016-07-01'),
    ]
    
    c.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", employees)
    
    # Sample users (password: "password123" for all)
    password_hash = hash_password("password123")
    users = [
        ('admin', password_hash, 'admin', None),
        ('alice', password_hash, 'student', 'S001'),
        ('bob', password_hash, 'student', 'S002'),
        ('carol', password_hash, 'student', 'S003'),
        ('david', password_hash, 'student', 'S004'),
        ('emma', password_hash, 'student', 'S005'),
        ('frank', password_hash, 'student', 'S006'),
        ('grace', password_hash, 'student', 'S007'),
        ('henry', password_hash, 'student', 'S008'),
        ('john', password_hash, 'employee', 'E001'),
        ('jane', password_hash, 'employee', 'E002'),
        ('mike', password_hash, 'employee', 'E003'),
        ('sarah', password_hash, 'employee', 'E004'),
        ('robert', password_hash, 'employee', 'E005'),
        ('maria', password_hash, 'employee', 'E006'),
        ('james', password_hash, 'employee', 'E007'),
    ]
    
    c.executemany("INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?)", users)
    
    # Sample courses
    courses = [
        ('CS101', 'Introduction to Programming', 'Computer Science', 'E001', 4, 'MWF 9:00-10:00 AM', 50, 35, 'Learn fundamental programming concepts using Python'),
        ('CS201', 'Data Structures', 'Computer Science', 'E007', 4, 'TTh 10:00-11:30 AM', 45, 30, 'Advanced data structures and algorithms'),
        ('EE101', 'Circuit Analysis', 'Electrical Engineering', 'E002', 3, 'MWF 11:00-12:00 PM', 40, 25, 'Basic electrical circuit theory and analysis'),
        ('ME101', 'Engineering Mechanics', 'Mechanical Engineering', 'E003', 3, 'TTh 2:00-3:30 PM', 40, 28, 'Statics and dynamics for engineers'),
        ('CE101', 'Surveying', 'Civil Engineering', 'E006', 3, 'MWF 1:00-2:00 PM', 35, 22, 'Land surveying techniques and instruments'),
        ('CS301', 'Database Systems', 'Computer Science', 'E001', 3, 'TTh 4:00-5:30 PM', 40, 32, 'Database design, SQL, and management'),
        ('EE201', 'Digital Electronics', 'Electrical Engineering', 'E002', 4, 'MWF 3:00-4:00 PM', 35, 30, 'Digital logic design and circuits'),
    ]
    
    c.executemany("INSERT INTO courses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", courses)
    
    # Sample events
    events = [
        ('Tech Fest 2026', 'Annual technology festival with competitions and exhibitions', '2026-02-15', '10:00 AM', 'Main Auditorium', 'Academic', 'Computer Science Dept'),
        ('Career Fair', 'Meet recruiters from top companies', '2026-02-20', '9:00 AM - 5:00 PM', 'Sports Complex', 'Career', 'Career Services'),
        ('Guest Lecture: AI in Healthcare', 'Dr. Sarah Chen from MIT discusses AI applications', '2026-01-25', '3:00 PM', 'Lecture Hall A', 'Academic', 'Admin'),
        ('Sports Day', 'Inter-department sports competition', '2026-03-10', '8:00 AM', 'Stadium', 'Sports', 'Athletics Dept'),
        ('Hackathon 2026', '24-hour coding marathon with prizes', '2026-02-28', '6:00 PM', 'CS Building Lab', 'Technical', 'Tech Club'),
        ('Alumni Meetup', 'Network with successful alumni', '2026-03-05', '6:00 PM', 'Conference Hall', 'Networking', 'Alumni Relations'),
        ('Cultural Night', 'Celebrating diversity through performances', '2026-02-14', '7:00 PM', 'Open Theater', 'Cultural', 'Student Council'),
    ]
    
    c.executemany("INSERT INTO events VALUES (null, ?, ?, ?, ?, ?, ?, ?)", events)
    
    # Sample announcements
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    announcements = [
        ('Mid-Term Exam Schedule Released', 'The mid-term examination schedule has been published on the student portal. Please check your schedule and note the dates.', today, 'high', 'all', 'admin'),
        ('Library Extended Hours', 'The library will remain open until midnight during exam week (Jan 20-27).', today, 'normal', 'all', 'admin'),
        ('New WiFi Password', 'Campus WiFi password has been updated. New password: Campus2026. Please update your devices.', today, 'high', 'all', 'admin'),
        ('Scholarship Applications Open', 'Merit-based scholarship applications are now open. Deadline: February 15, 2026.', today, 'normal', 'student', 'admin'),
        ('Faculty Meeting Reminder', 'All faculty members are requested to attend the monthly meeting on Jan 22 at 3 PM.', today, 'normal', 'employee', 'admin'),
        ('Parking Regulations Update', 'New parking permits required starting February 1st. Apply at Administration Office.', today, 'normal', 'all', 'admin'),
    ]
    
    c.executemany("INSERT INTO announcements VALUES (null, ?, ?, ?, ?, ?, ?)", announcements)
    
    # Sample resources
    resources = [
        ('Student Portal Guide', 'Complete guide to using the student portal', 'Document', 'https://portal.university.edu/guide', 'Academic', 'guide,portal,help'),
        ('Coding Practice Platform', 'Free coding practice and challenges', 'Website', 'https://leetcode.com', 'Technical', 'coding,practice'),
        ('IEEE Digital Library', 'Access to research papers and journals', 'Database', 'https://ieeexplore.ieee.org', 'Research', 'papers,research,ieee'),
        ('Mental Health Support', 'Counseling and wellness resources', 'Service', 'counseling@university.edu', 'Wellness', 'health,counseling,support'),
        ('Writing Center', 'Help with essays and research papers', 'Service', 'Building D, Room 201', 'Academic', 'writing,essays,help'),
        ('LaTeX Tutorial', 'Learn to write technical documents', 'Tutorial', 'https://www.overleaf.com/learn', 'Technical', 'latex,tutorial,documents'),
        ('Job Portal', 'Internship and job opportunities', 'Website', 'https://jobs.university.edu', 'Career', 'jobs,internship,career'),
    ]
    
    c.executemany("INSERT INTO resources VALUES (null, ?, ?, ?, ?, ?, ?)", resources)
    
    # Sample FAQs with categories
    faqs = [
        ("What are the library hours?", "The library is open Monday-Friday 8AM-10PM, Saturday 10AM-6PM, and Sunday 12PM-8PM.", "Facilities", 0),
        ("How do I reset my password?", "Visit the IT Help Desk in Building A, Room 101, or email support@university.edu with your student/employee ID.", "IT Support", 0),
        ("When is the registration deadline?", "Registration for Fall semester closes on August 15th. Late registration incurs a $100 fee.", "Academic", 0),
        ("Where can I find my class schedule?", "Log into the student portal and navigate to 'My Schedule' under the Academics tab.", "Academic", 0),
        ("How do I apply for leave?", "Employees can submit leave requests through the HR portal. Students should contact their academic advisor.", "HR", 0),
        ("What is the attendance policy?", "Students must maintain at least 75% attendance in each course to be eligible for final exams.", "Academic", 0),
        ("How do I pay my fees?", "Fees can be paid online through the student portal or in-person at the Finance Office in Building C.", "Finance", 0),
        ("Where is the cafeteria located?", "The main cafeteria is in Building B, ground floor. It serves breakfast (7-9AM), lunch (12-2PM), and dinner (6-8PM).", "Facilities", 0),
        ("How do I contact my professor?", "Professor contact information is available on the course syllabus and the university directory.", "Academic", 0),
        ("What are the exam dates?", "Mid-term exams are typically in October and March. Final exams are in December and May. Check the academic calendar for specific dates.", "Academic", 0),
        ("How do I book a study room?", "Study rooms can be booked through the library website up to 7 days in advance. Maximum 2 hours per booking.", "Facilities", 0),
        ("Is there parking available on campus?", "Yes, parking permits are required. Apply at Administration Office. Student parking: $100/semester, Employee parking: $200/year.", "Facilities", 0),
        ("How do I add/drop courses?", "Course add/drop can be done through the student portal during the first two weeks of the semester.", "Academic", 0),
        ("Where can I get tutoring help?", "Free tutoring services are available at the Learning Center, Building E. Book appointments online.", "Academic", 0),
        ("What health services are available?", "Campus Health Center provides medical services Mon-Fri 8AM-6PM. Emergency: Call Campus Security ext. 911.", "Health", 0),
    ]
    
    c.executemany("INSERT INTO faq (question, answer, category, views) VALUES (?, ?, ?, ?)", faqs)
    
    # Sample policies with categories
    policies = [
        ("Academic Integrity Policy", "All students must maintain academic honesty. Plagiarism, cheating, or any form of academic dishonesty will result in disciplinary action including possible expulsion. Students must cite sources properly and submit original work.", "Academic", "2020-01-01"),
        ("Attendance Policy", "Students must attend at least 75% of classes. Those falling below this threshold may be barred from final exams. Medical leave requires documentation.", "Academic", "2020-01-01"),
        ("Grading Policy", "Grades are based on: Assignments (20%), Mid-terms (30%), Finals (40%), and Participation (10%). Grade appeals must be submitted within 2 weeks of grade posting.", "Academic", "2020-01-01"),
        ("Leave Policy for Employees", "Employees are entitled to 20 days of paid leave per year. Leave must be approved by the department head at least one week in advance. Unused leave can be carried forward up to 10 days.", "HR", "2021-01-01"),
        ("Code of Conduct", "All members of the university community must treat each other with respect. Harassment, discrimination, or violence will not be tolerated. Report violations to the Dean of Students office.", "General", "2020-01-01"),
        ("Data Privacy Policy", "The university protects personal information according to GDPR standards. Student and employee data is confidential and used only for educational purposes.", "IT", "2022-01-01"),
        ("Research Ethics Policy", "All research involving human subjects requires ethics approval. Researchers must follow ethical guidelines and maintain participant confidentiality.", "Research", "2021-06-01"),
        ("Refund Policy", "Tuition refunds are available: 100% (week 1), 75% (week 2), 50% (week 3), no refund after week 3. Processing takes 4-6 weeks.", "Finance", "2020-01-01"),
    ]
    
    c.executemany("INSERT INTO policies (title, content, category, effective_date) VALUES (?, ?, ?, ?)", policies)
    
    conn.commit()
    conn.close()
    
    # Index all content in vector database
    print("Building vector search index...")
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT id, question, answer FROM faq")
    for row in c.fetchall():
        doc_text = f"Q: {row[1]}\nA: {row[2]}"
        add_to_vector_db(doc_text, f"faq_{row[0]}")
    
    c.execute("SELECT id, title, content FROM policies")
    for row in c.fetchall():
        doc_text = f"Policy: {row[1]}\n{row[2]}"
        add_to_vector_db(doc_text, f"policy_{row[0]}")
    
    c.execute("SELECT id, name, description FROM courses WHERE description IS NOT NULL")
    for row in c.fetchall():
        doc_text = f"Course: {row[1]}\n{row[2]}"
        add_to_vector_db(doc_text, f"course_{row[0]}")
    
    c.execute("SELECT id, title, description FROM events WHERE description IS NOT NULL")
    for row in c.fetchall():
        doc_text = f"Event: {row[1]}\n{row[2]}"
        add_to_vector_db(doc_text, f"event_{row[0]}")
    
    c.execute("SELECT id, title, description FROM resources WHERE description IS NOT NULL")
    for row in c.fetchall():
        doc_text = f"Resource: {row[1]}\n{row[2]}"
        add_to_vector_db(doc_text, f"resource_{row[0]}")
    
    conn.close()
    print("Sample data initialized successfully!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)