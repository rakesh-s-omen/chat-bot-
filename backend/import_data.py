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
