# 🚀 Quick Start Guide - Student/Employee Chatbot

Get your chatbot running in **5 minutes**!

---

## ⚡ Prerequisites

- **Python 3.8+** installed
- **2GB free disk space** (for AI models)
- **Modern web browser** (Chrome, Firefox, Edge, Safari)

---

## 📥 Step 1: Install Dependencies

Open your terminal and navigate to the project directory:

```bash
cd chatbot-system/backend
```

### Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

**Note:** First installation will download the AI model (~90MB). This only happens once!

---

## 🎯 Step 2: Start the Backend Server

```bash
python main.py
```

You should see:
```
Loading embedding model... (this may take a minute on first run)
Model loaded successfully!
Initializing sample data...
Building vector search index...
Sample data initialized successfully!
INFO:     Uvicorn running on http://127.0.0.1:8000
```

✅ **Backend is now running!**

---

## 🌐 Step 3: Open the Frontend

### Option A: Direct File Access
Simply open this file in your browser:
```
chatbot-system/frontend/index.html
```

### Option B: Local Server (Recommended)
Open a **new terminal** and run:

```bash
cd chatbot-system/frontend
python -m http.server 8080
```

Then visit: **http://localhost:8080**

---

## 🔑 Step 4: Login

Use these demo credentials:

### Admin Account
- **User ID:** `admin`
- **Password:** `password123`
- **Access:** Full system access

### Student Account
- **User ID:** `alice`
- **Password:** `password123`
- **Access:** Personal student records

### Employee Account
- **User ID:** `john`
- **Password:** `password123`
- **Access:** Personal employee records

---

## 💬 Step 5: Try the Chatbot!

After logging in, try asking:

### For Students:
- "What is my attendance?"
- "Show me my grades"
- "How much fees do I owe?"
- "What are the library hours?"

### For Employees:
- "How many leave days do I have?"
- "What is my salary?"
- "Show me my profile"
- "Tell me about the leave policy"

### For Everyone:
- "What are the library hours?"
- "Where is the cafeteria?"
- "How do I contact support?"

---

## 🎨 Explore the Features

### 1. Chat Interface
- Ask questions in natural language
- Get instant, personalized responses
- View suggested questions

### 2. Profile Section
- View your personal information
- Check attendance, grades, or leave balance
- See all your details in one place

### 3. Admin Panel (Admin Only)
- Add new FAQs
- Create policies
- Manage system content

---

## 🛠️ Troubleshooting

### Backend won't start?
- Make sure virtual environment is activated
- Check if port 8000 is available
- Verify all dependencies are installed

### Frontend can't connect?
- Ensure backend is running on port 8000
- Check browser console for errors
- Verify CORS settings

### Model loading is slow?
- First-time setup downloads ~90MB model
- Subsequent starts are much faster
- Be patient on first run!

### Login fails?
- Double-check credentials (case-sensitive)
- Ensure backend is running
- Check browser network tab for errors

---

## 📊 System Architecture

```
┌─────────────────────────────────────────┐
│         Frontend (Browser)              │
│  HTML/CSS/JS with Glassmorphism         │
└──────────────┬──────────────────────────┘
               │ REST API (JWT)
┌──────────────┴──────────────────────────┐
│         Backend (FastAPI)               │
│  • Authentication                       │
│  • AI Processing                        │
│  • Database Management                  │
└──────┬──────────────────┬───────────────┘
       │                  │
   ┌───┴────┐      ┌──────┴──────────┐
   │SQLite  │      │  Local AI       │
   │Database│      │  • Sentence     │
   └────────┘      │    Transformers │
                   │  • FAISS Search │
                   └─────────────────┘
```

---

## 🎯 Next Steps

### Customize Your Chatbot
1. Add your own data to the database
2. Modify the color scheme in `index.html`
3. Add custom intents in `main.py`
4. Create institution-specific FAQs

### Add Real Data
1. Replace sample data with actual records
2. Import from CSV files
3. Connect to existing databases
4. Integrate with your systems

### Deploy to Production
1. Change the secret key
2. Use PostgreSQL instead of SQLite
3. Add HTTPS/SSL
4. Set up monitoring
5. Configure backups

---

## 📚 Learn More

- **Full Documentation:** See `README.md`
- **Feature Guide:** See `FEATURES.md`
- **API Reference:** Visit http://localhost:8000/docs
- **Database Schema:** Check `FEATURES.md`

---

## 🆘 Need Help?

### Common Questions
- **Q: Can I use this offline?**  
  A: Yes! After initial setup, no internet required.

- **Q: Is it free?**  
  A: 100% free and open source. No API costs.

- **Q: Can I customize it?**  
  A: Absolutely! Modify colors, add features, change branding.

- **Q: Is my data secure?**  
  A: Yes! All data stays on your server. No external APIs.

### Support Resources
- Check the troubleshooting section above
- Review the full README.md
- Inspect browser console for errors
- Check backend terminal for logs

---

## ✅ Success Checklist

- [ ] Backend server running on port 8000
- [ ] Frontend accessible in browser
- [ ] Successfully logged in
- [ ] Sent a chat message
- [ ] Received a response
- [ ] Viewed profile section
- [ ] (Admin) Accessed admin panel

---

**Congratulations! 🎉**  
Your AI chatbot is now running!

Enjoy exploring the features and customizing it for your needs.

---

**Built with ❤️ for educational institutions**  
**100% Open Source • No API Keys • Privacy First**
