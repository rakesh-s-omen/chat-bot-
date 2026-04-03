# 🎓 HICAS AI Assistant - Student & Faculty Portal

A modern, intelligent chatbot system for HICAS (Hindustan Institute of Computer Applications and Sciences) with **5000+ students** and **393 faculty members**.

## ✨ Features

### 🎯 **Real Data Integration**
- ✅ **5000 Students** from actual HICAS CSV data
- ✅ **393 Faculty Members** from official records
- ✅ **Synthetic Data Generation**: Random CGPA (5-10), Attendance (60-100%), Fees, Salaries, etc.
- ✅ **Multiple Departments**: Computer Science, BCA, IT, AI & ML, Data Science, Commerce, English, and more

### 🤖 **AI-Powered Chatbot**
- Natural language processing for student/faculty queries
- Intelligent intent detection
- Context-aware responses
- Semantic search using FAISS vector database
- Sentence transformers for embeddings

### 🔐 **Secure Authentication**
- JWT-based authentication
- Role-based access control (Student, Faculty, Admin)
- Password hashing (SHA-256)
- Session management

### 💬 **Modern UI**
- Clean, minimalist design inspired by professional templates
- Smooth animations and transitions
- Responsive layout (mobile, tablet, desktop)
- Glassmorphism effects
- Professional color scheme

### 📊 **Comprehensive Data**
- Student records: CGPA, attendance, fees, grades, contact info
- Faculty records: salary, leave balance, designation, department
- FAQs and policies
- Course information
- Events and announcements

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- 2GB free disk space
- Modern web browser

### Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/rakesh-s-omen/chat-bot-.git
cd chat-bot-
```

2. **Setup AI Model (Ollama)**:
- Download and install [Ollama](https://ollama.com/download)
- Run: `ollama pull phi3`
- Keep Ollama running in the background

3. **Create virtual environment**:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

4. **Install dependencies**:
```bash
pip install -r backend/requirements.txt
```

5. **Import data**:
```bash
cd backend
python import_data.py
cd ..
```

6. **Start the server**:
Using the batch script (Windows):
```bash
run_project.bat
```
Or manually:
```bash
# In one terminal (Backend)
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# In another terminal (Frontend)
cd frontend
python -m http.server 8080
```

7. **Open the frontend**:
- Visit: `http://localhost:8080`

---

## 🔑 Login Credentials

### Admin Access
- **Username**: `admin`
- **Password**: `password123`

### Student Access
- **Username**: Any RegisterNumber (e.g., `82302630101`)
- **Password**: Same as RegisterNumber

### Faculty Access
- **Username**: Generated Faculty ID (check database)
- **Password**: Same as Faculty ID

---

## 📁 Project Structure

```
chatbot-system/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── import_data.py       # Data import script
│   ├── requirements.txt     # Python dependencies
│   └── chatbot.db          # SQLite database
├── frontend/
│   └── index.html          # Modern UI
├── hicas_students_simulated.csv    # 5000 students
├── hicas_faculty_data.csv          # 393 faculty
├── README.md
├── FEATURES.md
└── QUICKSTART.md
```

---

## 💾 Database Schema

### Students Table
```sql
- id (RegisterNumber)
- name
- department
- year (1-3)
- attendance (60-100%)
- grades (O, A+, A, B+, B, C)
- fees_due (0-50000)
- email
- phone
- address
- gpa (5.0-10.0)
```

### Employees (Faculty) Table
```sql
- id (Faculty ID)
- name
- designation (Professor, Associate Professor, Assistant Professor)
- department
- salary (40000-200000)
- leave_balance (5-25 days)
- email
- phone
- hire_date
```

---

## 🎨 UI Features

### Login Page
- Modern gradient background
- Clean, professional design
- Demo credentials display
- Smooth animations

### Chat Interface
- Welcome screen with quick questions
- Message bubbles with animations
- Typing indicator
- Auto-scroll
- Clean, minimalist design

### Profile Section
- Grid layout for information cards
- Hover effects
- Responsive design
- Easy-to-read format

### Admin Panel
- Add FAQs
- Add policies
- Success/error notifications
- Clean forms

---

## 🔧 API Endpoints

### Public
- `POST /login` - Authenticate user

### Protected (Requires JWT)
- `POST /chat` - Send message to chatbot
- `GET /me` - Get current user info
- `GET /my-records` - Get user's records
- `GET /courses` - Get course list
- `GET /events` - Get events
- `GET /announcements` - Get announcements

### Admin Only
- `POST /admin/add-user` - Create new user
- `POST /admin/add-faq` - Add FAQ
- `POST /admin/add-policy` - Add policy

---

## 💬 Example Queries

### Students
- "What is my attendance?"
- "Show me my CGPA"
- "How much fees do I owe?"
- "What is my grade?"
- "Show my profile"

### Faculty
- "How many leave days do I have?"
- "What is my salary?"
- "Show my department"
- "What is my designation?"

### General
- "What are the library hours?"
- "How do I pay fees?"
- "What is the attendance policy?"
- "Show me upcoming events"

---

## 📊 Statistics

- **Total Students**: 5,000
- **Total Faculty**: 393
- **Departments**: 30+
- **Programs**: UG & PG
- **Years**: 1-3 (UG), 1-2 (PG)

### Department Breakdown
- B.Sc Computer Science
- BCA (Bachelor of Computer Applications)
- B.Sc Information Technology
- B.Sc Computer Technology
- B.Sc CS with Cognitive Systems
- B.Sc AI & ML
- B.Sc Data Science & Analytics
- B.Com (Various specializations)
- BA English Literature
- BBA
- And many more...

---

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI
- **Database**: SQLite
- **Authentication**: JWT
- **AI/ML**: 
  - Sentence Transformers (`all-MiniLM-L6-v2`)
  - FAISS (vector search)
  - NLP for intent detection

### Frontend
- **Core**: HTML5, CSS3, JavaScript (ES6+)
- **Fonts**: Google Fonts (Poppins, Inter)
- **Design**: Modern, minimalist, responsive
- **No frameworks** - Pure vanilla JS

---

## 🎯 Key Improvements

### From Previous Version
1. ✅ **Real Data**: 5000+ students and 393 faculty from actual CSV files
2. ✅ **Modern UI**: Complete redesign with professional aesthetics
3. ✅ **Synthetic Data**: Random CGPA, attendance, fees, salaries
4. ✅ **Better UX**: Cleaner interface, smoother animations
5. ✅ **Responsive**: Works on all devices
6. ✅ **Professional**: Production-ready design

---

## 🔮 Future Enhancements

### Planned Features
- [x] Local LLM integration (Ollama)
- [ ] Voice input/output
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Mobile app (React Native)
- [ ] Email notifications
- [ ] Document upload
- [ ] Grade predictions
- [ ] Attendance alerts

---

## 📝 Notes

### Data Generation
- All CGPA values are randomly generated between 5.0 and 10.0
- Attendance is randomly generated between 60% and 100%
- Fees due are randomly generated between ₹0 and ₹50,000
- Faculty salaries are based on designation:
  - Professor: ₹80,000 - ₹1,50,000
  - Associate Professor: ₹60,000 - ₹1,00,000
  - Assistant Professor: ₹40,000 - ₹70,000
  - Professor & Head: ₹1,00,000 - ₹1,80,000

### Login System
- Students use their RegisterNumber as both username and password
- Faculty use their generated Faculty ID as both username and password
- Admin uses `admin` / `password123`

---

## 🐛 Troubleshooting

### Backend won't start
- Ensure virtual environment is activated
- Check if port 8000 is available
- Verify all dependencies are installed

### Frontend can't connect
- Ensure backend is running on port 8000
- Check browser console for errors
- Verify CORS settings

### Data import fails
- Ensure CSV files are in the correct location
- Check CSV file encoding (UTF-8)
- Verify database permissions

---

## 📄 License

This project is for educational purposes. Modify and use as needed.

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Local LLM integration
- Advanced analytics
- Mobile app
- Multi-language support
- Voice interface

---

## 📧 Support

For issues or questions:
- Check the documentation
- Review the code comments
- Inspect browser console
- Check backend logs

---

**Built with ❤️ for HICAS**  
**5000+ Students • 393 Faculty • 100% Real Data**
