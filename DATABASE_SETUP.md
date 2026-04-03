# SQLite Database Setup for VS Code

## Overview
Your chatbot system uses SQLite (`chatbot.db`) to store:
- User accounts and authentication
- Student and employee records
- FAQ, policies, courses
- Events and announcements
- Chat history and conversation context

## Installing VS Code Extension

### Method 1: Via VS Code Marketplace (Recommended)

1. **Open VS Code**
2. **Press** `Ctrl+Shift+X` to open Extensions panel
3. **Search for** one of these:
   - `SQLite Viewer` (by Florian Klampfer) - Simple, read-only
   - `SQLite` (by alexcvzz) - Full CRUD operations
4. **Click Install**

### Method 2: Via Command Line

Open terminal in VS Code and run:

```bash
# For SQLite Viewer (read-only, simple)
code --install-extension qwtel.sqlite-viewer

# OR for SQLite (full features)
code --install-extension alexcvzz.vscode-sqlite
```

## Using the Extension

### With SQLite Viewer (qwtel.sqlite-viewer)

1. **Navigate** to `backend/chatbot.db` in VS Code Explorer
2. **Click** on `chatbot.db` file
3. The database will open in a viewer tab
4. You can:
   - Browse all tables
   - View records
   - Filter and search data
   - Export data to CSV

### With SQLite (alexcvzz.vscode-sqlite)

1. **Open Command Palette**: `Ctrl+Shift+P`
2. **Type**: `SQLite: Open Database`
3. **Select**: `backend/chatbot.db`
4. The database appears in SQLite Explorer sidebar
5. You can:
   - Browse all tables
   - Run custom SQL queries
   - Edit records directly
   - Export query results

## Database Structure

Your `chatbot.db` contains these tables:

### Users & Auth
- **users** - Login credentials and roles
- **chat_history** - All chat conversations
- **conversation_context** - User session context

### Records
- **students** - Student information, grades, attendance
- **employees** - Faculty/staff information, salary, leave
- **courses** - Course catalog and enrollment

### Content
- **faq** - Frequently asked questions
- **policies** - University policies
- **events** - Campus events calendar
- **announcements** - Important notifications
- **resources** - Educational resources

## Example Queries

### View all users
```sql
SELECT user_id, role, linked_id FROM users;
```

### Check student records
```sql
SELECT id, name, department, year, attendance, gpa 
FROM students 
ORDER BY name;
```

### View recent chat history
```sql
SELECT user_id, message, response, timestamp 
FROM chat_history 
ORDER BY timestamp DESC 
LIMIT 20;
```

### Find employees by department
```sql
SELECT name, designation, department, email 
FROM employees 
WHERE department = 'Computer Science';
```

### Check upcoming events
```sql
SELECT title, date, time, location, category 
FROM events 
ORDER BY date;
```

## Managing the Database

### Backup Database
```bash
# In terminal
cp backend/chatbot.db backend/chatbot_backup_$(date +%Y%m%d).db
```

### Reset Database
Delete `chatbot.db` and restart the backend - it will recreate with fresh schema.

### Import Sample Data
```bash
# Already have import_data.py script
cd backend
python import_data.py
```

## Tips

1. **Read-only first**: Use SQLite Viewer for safe browsing
2. **Be careful with edits**: Use SQLite extension for editing, but back up first
3. **Check constraints**: Some fields have foreign key relationships
4. **Password hashes**: Passwords are SHA-256 hashed, can't view plaintext
5. **Refresh views**: After backend changes, refresh the extension view

## Troubleshooting

### Database locked
- Stop the FastAPI backend server first
- Close all database viewer tabs
- Reopen the database

### Can't see tables
- Make sure you've run the backend at least once
- Database is initialized on first startup

### Extension not working
- Make sure the file path is correct: `backend/chatbot.db`
- Try reloading VS Code: `Ctrl+Shift+P` → "Reload Window"

## Security Note

⚠️ **Never commit `chatbot.db` to Git** - it contains user data and password hashes!

Add to `.gitignore`:
```
backend/chatbot.db
backend/chatbot_backup_*.db
```
