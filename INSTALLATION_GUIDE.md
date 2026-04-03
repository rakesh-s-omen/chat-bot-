# 🚀 HICAS AI Assistant - Quick Installation & Run Guide

Follow these steps to set up the chatbot system on a new laptop or environment.

## 1. Prerequisites
Before starting, ensure you have the following installed:
* **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
* **Git**: [Download Git](https://git-scm.com/downloads)
* **Ollama**: Required for the local LLM. [Download Ollama](https://ollama.com/download)

## 2. Clone the Repository
Open your terminal (CMD or PowerShell) and run:
```bash
git clone https://github.com/rakesh-s-omen/chat-bot-.git
cd chat-bot-
```

## 3. Setup the AI Model (Ollama)
The chatbot uses the **Phi-3** model (3.8B parameters) which runs locally on your machine.
1. Install Ollama from the link above.
2. Open a terminal and run:
   ```bash
   ollama pull phi3
   ```
3. Keep the Ollama application running in the background.

## 4. One-Time Setup (Virtual Environment)
In the project root directory, run these commands to set up your Python environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install required dependencies
pip install -r backend/requirements.txt
```

## 5. Initialize the Database
Import the faculty and student data into the local SQLite database:
```bash
# Ensure venv is activated
cd backend
python import_data.py
cd ..
```

## 6. How to Run the System
You can start both the backend and frontend with a single command:
1. Simply double-click on `run_project.bat` in the root folder.
2. **OR** run it from the terminal:
   ```bash
   run_project.bat
   ```

### Accessing the App:
* **Frontend**: [http://localhost:8080](http://localhost:8080)
* **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

## 7. Login Credentials
You can use the following demo accounts once the system is running:

| Role | User ID | Password |
|------|---------|----------|
| **Student** | 22BCS101 | 22BCS101 |
| **Faculty** | FAC101 | FAC101 |
| **Admin** | admin | admin123 | (If registered)

---
**Note:** If you encounter any issues with the local LLM, ensure Ollama is installed and the `phi3` model is pulled successfully.
