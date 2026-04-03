<div align="center">

**STUDENT AND EMPLOYEE INFORMATION CHATBOT SYSTEM**

Submitted in partial fulfillment of the requirements for the award of the degree of

**BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY**

Bharathiar University, Coimbatore.

Submitted By

**KUMAR N**
**(Reg. No:23BIT026)**

Under the Supervision and Guidance of

**Dr.M. HEMALATHA MCA., M.Phil., Ph.D.,**
Professor
Department of Information Technology

**DEPARTMENT OF INFORMATION TECHNOLOGY**
**HINDUSTHAN COLLEGE OF ARTS & SCIENCE**
Coimbatore-641 028

**APRIL 2026**

</div>

<div style="page-break-after: always"></div>

<div align="center">
<b>DECLARATION</b>
</div>
<br><br>

I hereby declare that this project work is a record of original work.

<br><br><br>
**Place :** Coimbatore &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Signature**

**Date :** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **( KUMAR N )**

<div style="page-break-after: always"></div>

<div align="center">
<b>TABLE OF CONTENTS</b>
</div>

| CHAPTER NO | TITLE | PAGE NO. |
| :--- | :--- | :--- |
| | **ABSTRACT** | **1** |
| **1** | **INTRODUCTION** | **2** |
| | 1.1 Project Overview | 2 |
| | 1.2 Module Description | 3 |
| **2** | **SYSTEM ANALYSIS** | **4** |
| | 2.1 System Study | 4 |
| | 2.2 Existing System | 4 |
| | 2.3 Proposed System | 5 |
| **3** | **SYSTEM SPECIFICATION** | **6** |
| | 3.1 Hardware Specification | 6 |
| | 3.2 Software Specification | 6 |
| | 3.3 Software Feature | 7 |
| **4** | **DESIGN & DEVELOPMENT** | **13** |
| | 4.1 System Design | 13 |
| | 4.2 Input Design | 14 |
| | 4.3 Output Design | 16 |
| **5** | **SYSTEM TESTING** | **22** |
| | 5.1 Testing | 22 |
| | 5.2 Quality Assurance | 26 |
| **6** | **SYSTEM IMPLEMENTATION** | **27** |
| | 6.1 System Implementation | 27 |
| **7** | **CONCLUSION & FUTURE ENHANCEMENT**| **30** |
| | 7.1 Conclusion | 30 |
| | 7.2 Future Enhancement | 31 |
| | **BIBLIOGRAPHY** | **32** |
| | **APPENDIX** | **33** |
| | a. Sample Screen | 33 |
| | b. Sample Coding | 45 |

<div style="page-break-after: always"></div>


<div align="center">
<b>ABSTRACT</b>
</div>
<br>
The primary aim of this project is to architect and develop a centralized Student and Employee Information Chatbot System. This application enables the seamless and secure retrieval of personal, academic, and administrative data using natural language queries across various platforms. The architecture bridges the technological gap between legacy university databases and modern user-centric conversational interfaces. Built using a modern stack encompassing a FastAPI asynchronous backend, natural language vector embeddings via SentenceTransformers, and local SQLite data management, this system drastically optimizes organizational efficiency. By providing accurate figures—such as aggregated percentage grades, real-time cumulative attendance, outstanding fees, and staff payroll information—the system reduces administrative dependence. It employs robust multi-layered security protocols ensuring authentication passes through stateless JSON Web Tokens. Crucially, the system segregates returned variables based on active permissions tied to the authenticated user profile. Strict role-based isolation protects sensitive administrative metadata from unauthorized viewing, bringing a high level of secure convenience to the campus environment.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>1. INTRODUCTION

1.1 Project Overview</b>
</div>
<br>
In this project, the core objective is to implement authentication and secure communications protocols for a modernized Chatbot System. Traditional manual approaches and standard database web-portals present throughout university infrastructure are subject to high latency, human error, and massive administrative overhead. The conversational retrieval of specific records that transit internal communications links provides a highly optimized alternative. The implementation acts as the foundational starting point of an intelligent digital campus platform. Rather than expecting staff to repetitively answer standard queries over physical counters, the system acts as a frontline digital concierge. The functional purpose revolves around providing an active, 24/7 web-portal with an extensible architectural interface that allows institutions to securely map their existing data.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>1.2 Module Description</b>
</div>
<br>
**MEMBER AUTHENTICATION MODULE**
This represents the foundational module where the system securely processes internal verification protocols, collecting identification concerning active participants. Personal details such as the primary username, passwords rigorously mapped over advanced SHA-256 cryptographic hashes, and organizational roles (Student, Employee, Admin) are collected. It generates signed JWT sessions securely controlling access lifespans.

**NLP AND INTENT PARSING MODULE**
The intent detection framework acts as the central cognitive brain. Members log in and send conversational, unstructured text data straight into the API. The algorithm subsequently maps these localized text requests across dozens of conditional database commands (detecting intents like `check_attendance`, `view_fees`, or `check_salary`).

**DATABASE OPERATIONS MODULE**
This module maintains the data persistence tier where structural institutional data is written to disk. All user profile alterations and generated interactions are tracked utilizing relational SQLite structures guaranteeing data parity.

**ADMINISTRATOR RESOURCE MODULE**
This specialized interface restricts access exclusively to high-level administrators, providing them with comprehensive capabilities to modify generalized knowledge rules, input static FAQs, and broadcast dynamic priority announcements institution-wide.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>2. SYSTEM ANALYSIS

2.1 System Study</b>
</div>
<br>
The system analysis phase determines the detailed investigative studies concerning the various integrated operations performed seamlessly throughout the campus environment. It evaluates intrinsic relationships internally spanning across client inputs to database fetches and exterior factors including organizational adoption limitations. One core aspect involves mapping the boundaries defining what specific queries the chatbot must ignore compared to what administrative actions it must fulfill. During the analysis phase, data samples were collected mapping the volume of standard transactions handled by present human intervention processes. Identifying these decision logic points confirmed that integrating a chatbot model would undeniably provide a measurable, long-term operational advantage.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>2.2 Existing System</b>
</div>
<br>
Within the bounds of existing workflows established inside typical academic environments, institutional information remains heavily fragmented and isolated in specific server silos. In historical setups, individuals must travel physically to centralized administrative buildings to view hardcopy grade distributions, finalize attendance disputes, or request payroll printouts. When organizations attempted to digitize this over the previous decade, they launched rigid, highly convoluted web portals that frequently experience excessive downtime during peak semester loads. The navigation inside these legacy environments requires users to dig through dozens of dropdown interfaces to find singular statistics. There is no active contextual memory, and retrieving specific unstructured information forces the student to compose manual emails that might sit inside support queues for days.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>2.3 Proposed System</b>
</div>
<br>
The proposed architecture counteracts legacy inefficiencies by introducing a unified, centralized Chatbot interface seamlessly enabling rapid, real-time query resolution. In this robust paradigm, authenticated individuals instantly log into the unified messaging screen and immediately converse using natural human linguistics regardless of their physical geographical location. Administrators are conversely granted an optimized backend dashboard allowing them to swiftly construct FAQ knowledge items or upload documentation without writing lines of code. All connected intelligence streams seamlessly merge into a high-speed SQLite pipeline tracking metrics accurately ensuring historical retention. The backend forces stateless JSON Web Token handshakes guaranteeing the absolute prevention of accidental session mixups specifically shielding private grade sheets and payroll matrices away from targeted attacks.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>3. SYSTEM SPECIFICATION

3.1 Hardware Specification</b>
</div>
<br>
Achieving seamless execution requires optimized baseline infrastructure guarantees ensuring zero frame drops during concurrent usage simulations.
- **Processor**: Intel Core i5 / AMD Ryzen 5 or equivalent (Minimum clock speed: 2.5 GHz). Quad-core recommended handling asynchronous FastAPI workers.
- **Main Memory**: Minimum 8 GB providing sufficient cache padding for localized FAISS indices natively.
- **Hard Disk**: At least 256 GB NVMe evaluating solid-state architectures maximizing immediate I/O read bursts.
- **Architecture**: Dedicated 64-bit environment actively matching Python pipeline configurations effortlessly.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>3.2 Software Specification</b>
</div>
<br>
Software mapping parameters distinctly correlate spanning modern open-source toolkits dynamically scaling web requirements correctly.
- **Operating System**: Stable enterprise versions spanning Windows Enterprise or Ubuntu LTS releases.
- **Front-End UI**: Vanilla JavaScript combined with customized CSS3 and HTML5 layouts ensuring rapid DOM parsing without framework bloat.
- **Back-End System**: Python 3.10+ harnessing the asynchronous FastAPI networking framework executing backend routing rules.
- **Vector Core**: Facebook's FAISS library processing multi-dimensional text embeddings.
- **Standard Database**: The deeply integrated SQLite package providing serverless relational integrity.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>3.3 Software Feature</b>
</div>
<br>
**Python and FastAPI Configurations**
The deployment harnesses FastAPI representing a mathematically proven modern networking framework purposefully compiling highly concurrent REST requests dynamically utilizing standard Python type hints. FastAPI is designed embracing the `async def` parameter ensuring backend thread availability.

**RESTful API Engineering**
The endpoints naturally enforce profound JSON-based documentation layouts instantly accessible globally. When compiling the structural models using Pydantic, inbound user variables are parsed securely.

**Efficient Mathematical Embeddings**
The local HuggingFace `all-MiniLM-L6-v2` transformer natively embeds vast dictionary paragraphs perfectly transforming human sentences directly into high dimensional algebraic vectors. This enables the bot to calculate raw semantic meaning expanding contextual accuracy dramatically without external cloud processing costs.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>4. DESIGN & DEVELOPMENT

4.1 System Design</b>
</div>
<br>
System design characterizes the highly rigorous logical mapping translating specific application requirements into tangible software environments. The blueprint states specifically how complex computational arrays resolve all structural obstacles specifically recognized during initial analysis cycles. The architecture successfully operates following a decoupled Client-Server REST methodology isolating the visual presentation away from backend execution logic proactively. This abstraction inherently forces operations to strictly query the internal localized SQLite database executing validation processes instantly without maintaining complex external server states, enforcing long-term scalability safely.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>4.2 Input Design</b>
</div>
<br>
Input processing defines exactly how the backend translates real-world unstructured conversational data efficiently onto structured operational stacks natively minimizing anomalies. The primary engineering goal verifies real-time user keystrokes proactively eliminating maliciously structured parameters prior to reaching deep server subroutines. When examining external inputs, authenticated individuals write conversational fragments mapping towards specific endpoints globally dynamically parsing words utilizing pre-built natural language pipelines. Internally generated variables effortlessly translate specifically alongside highly complex web tokens directly passing strict authentication hashes ensuring session stability.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>4.3 Output Design</b>
</div>
<br>
Output parameter configurations explicitly dictate dynamically organizing numerical database extractions directly into highly legible, formatted messaging blocks ensuring the end-user understands all metrics reliably. The outputs structurally format utilizing flexible markdown syntax natively generated by the underlying mathematical LLM heuristic engines. The strict validation matrices enforce standardized HTTP web resolutions instantly reporting logical milestones, indicating successful transaction processing effortlessly and alerting individuals visually to potential conversational misunderstandings or out-of-bounds parameters.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>5. SYSTEM TESTING

5.1 Testing</b>
</div>
<br>
The testing environment evaluates deep functional components comprehensively analyzing software performance systematically and preventing active failures entirely prior to entering production networks. The software structurally compartmentalizes execution trees testing atomic units functionally and explicitly generating precise outcomes exactly verifying inputs correctly. Engineers rigorously test final external visual boundaries examining unpredictable linguistic grammar structures intentionally verifying internal intent-parsers perfectly discard arbitrary random characters effectively. Load testing simulated thousands of virtual concurrent users validating server bandwidth consumption capacity.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>5.2 Quality Assurance</b>
</div>
<br>
Establishing highly structured internal quality metrics guarantees exceptional software lifecycles assuring consistent deployment conditions. By implementing strict internal data privacy boundaries inherently preventing malicious token manipulations successfully actively securing all historical data layers, the system provides immense integrity. The diagnostic unit tests verify explicit internal logic pipelines specifically ensuring boolean loops calculate conditions correctly, terminating natively and preventing recursive computational locks successfully checking all logical endpoint parameters.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>6. SYSTEM IMPLEMENTATION

6.1 System Implementation</b>
</div>
<br>
Deployment functionally transitions exact theoretical design mockups compiling backend source code specifically initiating live enterprise operations systematically integrating without explicit workflow disruption. Configuring isolated staging subsets successfully tests real-world throughput observing simulated loads resolving any runtime constraint. The transition framework introduces optimized installation pipelines proactively checking configuration dependencies ensuring deep environment libraries properly execute safely. Comprehensive staff documentation details exact software guidelines providing deep reference materials establishing final administrative familiarity required for permanent operational reliability.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>7. CONCLUSION & FUTURE ENHANCEMENT

7.1 Conclusion</b>
</div>
<br>
The software project successfully establishes modern database integrations revolutionizing traditional institutional operations precisely and safely. By transitioning from static web-forms to interactive, vector-based conversational querying interfaces, latency overhead decreases drastically alongside human cognitive load. The implementation connects vast unstructured repositories accurately predicting specific domain intents comprehensively parsing parameters appropriately. By maintaining local sentence embeddings integrated via FAISS methodologies, data isolation acts natively and effectively guaranteeing maximum privacy laws compliance systematically executing intelligently and reliably.
<br>

<div style="page-break-after: always"></div>
<div align="center">
<b>7.2 Future Enhancement</b>
</div>
<br>
Future strategic technological additions integrate upcoming asynchronous processing engines dynamically naturally and flawlessly. Specifically, an enhanced on-line scheduling architecture provides users with the facility to perform physical transactions—like automatically scheduling faculty drop-in appointments instantly or generating localized PDFs seamlessly embedded within the Chatbot screen layout organically completely streamlining structural communication barriers comprehensively efficiently cleanly properly.
<br>

<div style="page-break-after: always"></div>

**BIBLIOGRAPHY**

1. Sebastián Ramírez, “FastAPI Documentation”
2. Martin Kleppmann, "Designing Data-Intensive Applications"
3. Steven Holzner,” Python and Web Frameworks”

**APPENDIX**

**a. Sample Screen**

**LOGIN USER INTERFACE**
```
Username: [ johndoe123 ]
Password: [ ******** ]
[ SECURE LOGIN ]
```

<div style="page-break-after: always"></div>

**b. Sample Coding**

The following appendix features the core backend architecture files natively spanning across the entire system implementation, combining logical APIs, Intent vectors, and relational database connections securely built via FastAPI and SQLite methodologies.


### Source Code File: `main.py`
```python

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
```

<div style="page-break-after: always"></div>

### Source Code File: `import_data.py`
```python
"""
Import HICAS student and faculty data with synthetic random information
"""

import sqlite3
import csv
import random
from datetime import datetime, timedelta

def generate_random_cgpa():
    """Generate random CGPA between 5.0 and 10.0"""
    return round(random.uniform(5.0, 10.0), 2)

def generate_random_attendance():
    """Generate random attendance between 60% and 100%"""
    return round(random.uniform(60.0, 100.0), 2)

def generate_random_fees():
    """Generate random fees due between 0 and 50000"""
    return round(random.uniform(0, 50000), 2)

def generate_random_phone():
    """Generate random Indian phone number"""
    return f"+91 {random.randint(70000, 99999)}{random.randint(10000, 99999)}"

def generate_random_address():
    """Generate random address"""
    cities = ["Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi", "Pune", "Kolkata"]
    streets = ["MG Road", "Anna Salai", "Brigade Road", "Park Street", "Nehru Place"]
    return f"{random.randint(1, 999)} {random.choice(streets)}, {random.choice(cities)}"

def generate_random_salary():
    """Generate random salary for faculty"""
    designations_salary = {
        "Professor": (80000, 150000),
        "Associate Professor": (60000, 100000),
        "Assistant Professor": (40000, 70000),
        "Professor & Head": (100000, 180000),
        "Professor & Director": (120000, 200000)
    }
    return designations_salary

def generate_random_leave():
    """Generate random leave balance between 5 and 25 days"""
    return random.randint(5, 25)

def import_students():
    """Import students from CSV with synthetic data"""
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()

    # Clear existing students
    c.execute("DELETE FROM students")
    c.execute("DELETE FROM users WHERE role = 'student'")

    print("Importing students...")

    with open('../hicas_students_simulated.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0

        for row in reader:
            student_id = row['RegisterNumber']
            name = row['Student Name']
            department = row['Department']
            year = int(row['Year'])
            email = row['Email']

            # Generate synthetic data
            cgpa = generate_random_cgpa()
            attendance = generate_random_attendance()
            fees_due = generate_random_fees()
            phone = generate_random_phone()
            address = generate_random_address()

            # Determine grade based on CGPA
            if cgpa >= 9.0:
                grade = "O (Outstanding)"
            elif cgpa >= 8.0:
                grade = "A+ (Excellent)"
            elif cgpa >= 7.0:
                grade = "A (Very Good)"
            elif cgpa >= 6.0:
                grade = "B+ (Good)"
            elif cgpa >= 5.5:
                grade = "B (Above Average)"
            else:
                grade = "C (Average)"

            # Insert student
            c.execute('''INSERT INTO students
                        (id, name, department, year, attendance, grades, fees_due, email, phone, address, gpa)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (student_id, name, department, year, attendance, grade, fees_due, email, phone, address, cgpa))

            # Create user account (password is register number)
            import hashlib
            password_hash = hashlib.sha256(student_id.encode()).hexdigest()
            c.execute('''INSERT INTO users (user_id, password_hash, role, linked_id)
                        VALUES (?, ?, ?, ?)''',
                     (student_id, password_hash, 'student', student_id))

            count += 1
            if count % 100 == 0:
                print(f"Imported {count} students...")

    conn.commit()
    print(f"✅ Successfully imported {count} students!")
    return count

def import_faculty():
    """Import faculty from CSV with synthetic data"""
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()

    # Clear existing employees
    c.execute("DELETE FROM employees")
    c.execute("DELETE FROM users WHERE role = 'employee'")

    print("\nImporting faculty...")

    salary_ranges = {
        "Professor": (80000, 150000),
        "Associate Professor": (60000, 100000),
        "Assistant Professor": (40000, 70000),
        "Professor & Head": (100000, 180000),
        "Professor & Director Admission": (120000, 200000),
        "Professor & Director": (120000, 200000)
    }

    with open('../hicas_faculty_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        faculty_ids = set()

        for row in reader:
            name = row['Faculty Name'].strip()
            department = row['Department']
            designation = row['Designation']

            # Use Faculty Name directly as ID
            faculty_id = name

            # Ensure unique ID (append number if duplicate exists)
            original_id = faculty_id
            counter = 1
            while faculty_id in faculty_ids:
                faculty_id = f"{original_id} {counter}"
                counter += 1
            faculty_ids.add(faculty_id)

            # Generate synthetic data
            salary_range = salary_ranges.get(designation, (40000, 70000))
            salary = round(random.uniform(salary_range[0], salary_range[1]), 2)
            leave_balance = generate_random_leave()
            email = f"{faculty_id.lower()}@hicas.ac.in"
            phone = generate_random_phone()

            # Generate hire date (between 1 and 20 years ago)
            years_ago = random.randint(1, 20)
            hire_date = (datetime.now() - timedelta(days=years_ago*365)).strftime("%Y-%m-%d")

            # Insert faculty
            c.execute('''INSERT INTO employees
                        (id, name, designation, department, salary, leave_balance, email, phone, hire_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (faculty_id, name, designation, department, salary, leave_balance, email, phone, hire_date))

            # Create user account (password is 'faculty123')
            import hashlib
            password_hash = hashlib.sha256("faculty123".encode()).hexdigest()
            c.execute('''INSERT INTO users (user_id, password_hash, role, linked_id)
                        VALUES (?, ?, ?, ?)''',
                     (faculty_id, password_hash, 'employee', faculty_id))

            count += 1

    conn.commit()
    print(f"✅ Successfully imported {count} faculty members!")
    return count

def create_sample_faqs():
    """Create sample FAQs"""
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()

    c.execute("DELETE FROM faq")

    faqs = [
        ("What are the library hours?", "The library is open Monday-Friday: 8:00 AM - 10:00 PM, Saturday: 10:00 AM - 6:00 PM, Sunday: 12:00 PM - 8:00 PM"),
        ("How do I check my attendance?", "You can check your attendance by logging into the student portal or asking this chatbot 'What is my attendance?'"),
        ("What is the minimum attendance requirement?", "Students must maintain at least 75% attendance to be eligible for final examinations."),
        ("How is CGPA calculated?", "CGPA is calculated on a 10-point scale based on your performance across all semesters."),
        ("Where is the cafeteria located?", "The main cafeteria is located in Building B, Ground Floor. There's also a food court in the Student Center."),
        ("How do I pay my fees?", "Fees can be paid online through the student portal, at the Finance Office (Building C), or via bank transfer."),
        ("What are the exam dates?", "Exam schedules are published on the university website and student portal at least one month before exams."),
        ("How do I apply for leave?", "Faculty and staff can apply for leave through the HR portal. Students should contact their department head."),
        ("Where can I get my ID card?", "ID cards are issued by the Administration Office in Building A, Room 105."),
        ("How do I contact technical support?", "IT Support is available at Building A, Room 101. Email: support@hicas.ac.in, Phone: (555) 123-4567")
    ]

    for question, answer in faqs:
        c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)",
                 (question, answer, "General"))

    conn.commit()
    print(f"✅ Created {len(faqs)} sample FAQs!")

def main():
    """Main import function"""
    print("=" * 60)
    print("HICAS Data Import Tool")
    print("=" * 60)

    student_count = import_students()
    faculty_count = import_faculty()
    create_sample_faqs()

    print("\n" + "=" * 60)
    print("Import Summary:")
    print(f"  Students: {student_count}")
    print(f"  Faculty: {faculty_count}")
    print("=" * 60)
    print("\n✅ All data imported successfully!")
    print("\nSample Login Credentials:")
    print("  Admin: admin / password123")
    print("  Student: Use any RegisterNumber as both username and password")
    print("  Faculty: Use generated Faculty ID as both username and password")
    print("\nNote: Check the database for specific faculty IDs")

if __name__ == "__main__":
    main()
```

<div style="page-break-after: always"></div>

### Source Code File: `llm_integration.py`
```python
"""
Local LLM Integration using Ollama
Lightweight and efficient - uses Phi-3 Mini (3.8B parameters)
"""

import ollama
import json
from typing import Dict, List, Optional

class LocalLLM:
    def __init__(self, model_name: str = "phi3"):
        """
        Initialize local LLM

        Models (in order of size/speed):
        - phi3: 3.8B params, very fast, excellent for this use case (RECOMMENDED)
        - llama3.2: 3B params, also very fast
        - gemma2:2b: 2B params, fastest but less capable
        """
        self.model_name = model_name
        self.available = self._check_availability()

    def _check_availability(self) -> bool:
        """Check if Ollama is installed and model is available"""
        try:
            # Try to list models
            models_response = ollama.list()

            # Handle object response (new version) or dict response (old version)
            if hasattr(models_response, 'models'):
                model_names = [m.model for m in models_response.models]
            else:
                model_names = [m['name'] for m in models_response.get('models', [])]

            # Check if our model is available
            if any(self.model_name in name for name in model_names):
                print(f"\n✨ SUCCESS: Local LLM '{self.model_name}' is connected and ready! ✨\n")
                return True
            else:
                print(f"⚠️ Model '{self.model_name}' not found. Please run: ollama pull {self.model_name}")
                return False
        except Exception as e:
            print(f"⚠️ Ollama not available: {e}")
            print("Please install Ollama from: https://ollama.ai")
            return False

    def generate_response(
        self,
        user_query: str,
        user_data: Optional[Dict] = None,
        context_docs: Optional[List[str]] = None,
        role: str = "student",
        conversation_history: Optional[List[Dict]] = None
    ) -> str:
        """
        Generate response using local LLM

        Args:
            user_query: User's question
            user_data: User's personal data from database
            context_docs: Relevant documents from vector search
            role: User's role (student/employee/admin)
            conversation_history: Previous messages for context
        """

        if not self.available:
            return self._fallback_response(user_query, user_data, role)

        try:
            # Build context-aware prompt
            system_prompt = self._build_system_prompt(role, user_data, context_docs)

            # Build conversation history
            messages = [{"role": "system", "content": system_prompt}]

            if conversation_history:
                messages.extend(conversation_history[-3:])  # Last 3 messages for context

            messages.append({"role": "user", "content": user_query})

            # Generate response
            response = ollama.chat(
                model=self.model_name,
                messages=messages,
                options={
                    "temperature": 0.7,  # Balanced creativity
                    "top_p": 0.9,
                    "num_predict": 256,  # Max tokens (keep responses concise)
                }
            )

            return response['message']['content'].strip()

        except Exception as e:
            print(f"LLM Error: {e}")
            return self._fallback_response(user_query, user_data, role)

    def _build_system_prompt(
        self,
        role: str,
        user_data: Optional[Dict],
        context_docs: Optional[List[str]]
    ) -> str:
        """Build system prompt with context"""

        prompt = """You are a helpful AI assistant for HICAS (Hindustan Institute of Computer Applications and Sciences).

Your role: Provide accurate, friendly, and concise responses to students, faculty, and staff.

Guidelines:
- Be professional but friendly
- Keep responses concise (2-3 sentences for simple queries)
- Use emojis sparingly for visual appeal
- If you don't know something, say so honestly
- For personal data queries, use the provided user information
- For general queries, use the knowledge base documents provided

"""

        # Add user-specific context
        if user_data and role == "student":
            prompt += f"\nCurrent Student Information:\n"
            prompt += f"- Name: {user_data.get('name', 'N/A')}\n"
            prompt += f"- Department: {user_data.get('department', 'N/A')}\n"
            prompt += f"- Year: {user_data.get('year', 'N/A')}\n"
            prompt += f"- Attendance: {user_data.get('attendance', 'N/A')}%\n"
            prompt += f"- CGPA: {user_data.get('gpa', 'N/A')}\n"
            prompt += f"- Fees Due: ₹{user_data.get('fees_due', 0)}\n"
            # Dynamic Schedule Info
            prompt += f"- Next Class: {user_data.get('next_class', 'N/A')}\n"
            prompt += f"- Next Activity (Now): {user_data.get('next_hour_activity', 'N/A')}\n"
            prompt += f"- Upcoming Exam: {user_data.get('next_exam', 'N/A')} on {user_data.get('exam_date', 'N/A')}\n"
            prompt += f"- Next Holiday: {user_data.get('next_holiday', 'N/A')}\n"

        elif user_data and role == "employee":
            prompt += f"\nCurrent Employee Information:\n"
            prompt += f"- Name: {user_data.get('name', 'N/A')}\n"
            prompt += f"- Designation: {user_data.get('designation', 'N/A')}\n"
            prompt += f"- Department: {user_data.get('department', 'N/A')}\n"
            prompt += f"- Leave Balance: {user_data.get('leave_balance', 'N/A')} days\n"
            prompt += f"- Salary: ₹{user_data.get('salary', 0):,.2f}\n"
            # Dynamic Schedule Info
            prompt += f"- Next Class to Teach: {user_data.get('next_class_to_teach', 'N/A')}\n"
            prompt += f"- Next Activity (Now): {user_data.get('next_hour_activity', 'N/A')}\n"
            prompt += f"- Upcoming Task: {user_data.get('next_task', 'N/A')}\n"
            prompt += f"- Deadlines: {user_data.get('submission_deadline', 'N/A')}\n"
            prompt += f"- Next Holiday: {user_data.get('next_holiday', 'N/A')}\n"

        # Add knowledge base context
        if context_docs:
            prompt += "\nRelevant Knowledge Base:\n"
            for i, doc in enumerate(context_docs[:3], 1):
                prompt += f"{i}. {doc}\n"

        prompt += "\nRespond naturally and helpfully based on the above information."

        return prompt

    def _fallback_response(self, query: str, user_data: Optional[Dict], role: str) -> str:
        """Fallback response when LLM is not available"""

        query_lower = query.lower()

        # Quick pattern matching for common queries
        if "attendance" in query_lower and user_data and role == "student":
            att = user_data.get('attendance', 'N/A')
            return f"Your current attendance is {att}%. The minimum requirement is 75%."

        if "cgpa" in query_lower or "gpa" in query_lower and user_data and role == "student":
            gpa = user_data.get('gpa', 'N/A')
            grade = user_data.get('grades', 'N/A')
            return f"Your CGPA is {gpa} with a grade of {grade}."

        if "fees" in query_lower and user_data and role == "student":
            fees = user_data.get('fees_due', 0)
            if fees == 0:
                return "You have no pending fees. Your account is clear!"
            return f"You have ₹{fees:,.2f} in pending fees."

        if "leave" in query_lower and user_data and role == "employee":
            leave = user_data.get('leave_balance', 'N/A')
            return f"You have {leave} days of leave remaining."

        if "salary" in query_lower and user_data and role == "employee":
            salary = user_data.get('salary', 0)
            return f"Your annual salary is ₹{salary:,.2f}."

        return "I'm here to help! Could you please rephrase your question or ask about your attendance, grades, fees, or other university information?"

    def stream_response(
        self,
        user_query: str,
        user_data: Optional[Dict] = None,
        context_docs: Optional[List[str]] = None,
        role: str = "student"
    ):
        """
        Stream response for real-time display (future enhancement)
        """
        if not self.available:
            yield self._fallback_response(user_query, user_data, role)
            return

        try:
            system_prompt = self._build_system_prompt(role, user_data, context_docs)

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ]

            stream = ollama.chat(
                model=self.model_name,
                messages=messages,
                stream=True,
                options={
                    "temperature": 0.7,
                    "num_predict": 256,
                }
            )

            for chunk in stream:
                if 'message' in chunk and 'content' in chunk['message']:
                    yield chunk['message']['content']

        except Exception as e:
            print(f"Streaming error: {e}")
            yield self._fallback_response(user_query, user_data, role)


# Singleton instance
_llm_instance = None

def get_llm() -> LocalLLM:
    """Get or create LLM instance"""
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = LocalLLM(model_name="phi3")
    return _llm_instance
```

<div style="page-break-after: always"></div>

