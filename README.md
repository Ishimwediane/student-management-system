# Student Course Management System

A console-based Python application to manage students, courses, and enrollments.  
This project demonstrates **Python fundamentals**, **OOP principles**, and **modular programming**.

---

## Features

- Add Undergraduate or Graduate students
- Add courses with instructors
- Enroll students in courses
- List students in a course
- Update course details
- Remove students from courses
- List all courses
- Simple CLI interface

---

## Project Structure

student_course_management/
│
├─ models/
│ ├─ init.py
│ ├─ student.py
│ └─ course.py
│
├─ main.py
└─ README.md


- `models/student.py` → Contains `Student`, `Undergraduate`, and `Graduate` classes
- `models/course.py` → Contains `Course` class
- `main.py` → CLI application to interact with students and courses

---

## Setup Instructions

1. **Install Python 3.11+**  
   Check installation:  
   ```bash
   python --version
