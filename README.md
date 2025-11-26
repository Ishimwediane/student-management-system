# Student Course Management System

A **console-based Python application** to manage students, courses, enrollments, and grades.  
This project demonstrates **Python fundamentals**, **OOP principles**, **modular programming**, and **data handling** in a simple CLI environment.

---

##  Features

### Student Management
- Add **Undergraduate** or **Graduate** students with comprehensive validation:
  - Names only accept letters and spaces
  - Gender must be `male` or `female`
  - Email must be valid (contain `@` and `.`)
  - Unique student IDs
  - Field of study specification

### Course Management
- Add **courses** with unique IDs
- Optionally restrict courses to certain levels or fields
- Update course titles
- View all available courses

### Enrollment & Grading
- Enroll students in one or more courses
- Automatic validation of level and field restrictions
- Set **grades** for students per course (0–100)
- Calculate **total average grades** per student
- Remove students from courses

### Academic Reporting
- Show **student transcripts** including:
  - All enrolled courses and grades
  - Total average grade
  - Academic status classification:
    - **First Class** (70–100)
    - **Second Upper** (60–69)
    - **Second Lower** (50–59)
    - **Pass** (40–49)
    - **Fail** (0–39)
- List all students in a course with their grades

### User Interface
- Simple **Command-Line Interface (CLI)**
- Input validation and error handling
- Clear menu system

---

##  Project Structure

```
student_course_management/
│
├── models/
│   ├── __init__.py
│   ├── student.py          # Student, Undergraduate, Graduate classes with validation
│   └── course.py  
    └── enrollment.py         # Course and Enrollment classes
│
├── main.py                 # CLI application to interact with students and courses
├── requirements.txt        # Python version and optional packages
└── README.md              # Project documentation
```

---

##  Setup Instructions

### 1. Install Python 3.11+

Check your Python installation:
```bash
python --version
```

### 2. Clone the repository

```bash
git clone <your-repo-url>
cd student_course_management
```

### 3. Install dependencies (if any)

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```
---

##  Usage

### Main Menu Options

```
--- Student Course Management System ---
1. Add Student
2. Add Course
3. Enroll Student in Course
4. Set Grade for Student in Course
5. List Students in a Course
6. Show Student Transcript
7. Update Course
8. Remove Student from Course
9. List All Courses
10. List All Students
0. Exit
```

### Workflow

1. **Add Students**: Provide name (letters only), ID, gender, email, level, and field of study
2. **Add Courses**: Provide course title and unique course ID. Optionally specify allowed levels or fields
3. **Enroll Students**: Students can enroll in multiple courses, respecting allowed levels/fields
4. **Set Grades**: Assign grades per course (0–100)
5. **View Transcript**: Shows all courses, grades, total average, and academic status
6. **List Students in a Course**: Displays enrolled students and their grades
7. **Update Course**: Change the course title
8. **Remove Student**: Remove a student from a specific course

---

##  Example Usage

### Adding a Student

```
Select an option: 1
Name: Alice Johnson
Student ID: U123
Gender (male/female): female
Email: alice@gmail.com
Level (undergraduate/graduate): undergraduate
Field of study: Computer Science

✔ Student added: Alice Johnson - Undergraduate in Computer Science
```

### Adding a Course

```
Select an option: 2
Course Title: Introduction to Programming
Course ID: CS101
Allowed Level (undergraduate/graduate/all): undergraduate
Allowed Field (or press Enter for all): Computer Science

✔ Course added: Introduction to Programming (CS101)
```

### Enrolling a Student

```
Select an option: 3
Student ID: U123
Course ID: CS101

✔ Alice Johnson enrolled in Introduction to Programming
```

### Setting a Grade

```
Select an option: 4
Student ID: U123
Course ID: CS101
Grade (0-100): 85

✔ Grade set: Alice Johnson scored 85 in Introduction to Programming
```

### Viewing Student Transcript

```
Select an option: 6
Student ID: U123

========================================
TRANSCRIPT - Alice Johnson (U123)
Undergraduate - Computer Science
========================================

Course: Introduction to Programming (CS101)
Grade: 85

Course: Data Structures (CS102)
Grade: 78

----------------------------------------
Total Average: 81.5
Academic Status: First Class
========================================
```

---

##  Key Features Explained

### Input Validation

- **Name**: Require
- **Gender**: Must be exactly "male" or "female"
- **Email**: Must contain "@" and "."
- **Grade**: Must be between 0 and 100
- **Student ID**: Must be unique

### Course Restrictions

Courses can be restricted by:
- **Level**: Undergraduate-only, Graduate-only, or open to all
- **Field of Study**: Specific field requirements or open to all

Students can only enroll if they meet the course requirements.

### Academic Status Classification

| Grade Range | Status |
|-------------|--------|
| 70–100 | First Class |
| 60–69 | Second Upper |
| 50–59 | Second Lower |
| 40–49 | Pass |
| 0–39 | Fail |

---



##  Future Enhancements

- [ ] Export transcripts to PDF
- [ ] Pretty table formatting using tabulate
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] GUI interface (Tkinter/PyQt)
- [ ] GPA calculation (weighted credits)
- [ ] Student search and filter functionality
- [ ] Email notifications for grades
- [ ] Course capacity limits
- [ ] Waitlist management

---

##  Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Add docstrings to all functions and classes
- Include unit tests for new features
- Update README.md if needed

---

##  Testing

To run tests (if implemented):

```bash
python -m pytest tests/
```

---

##  Contact

For questions or feedback, please contact:  
 **ishimwediane400@gmail.com**

---

##  Acknowledgments

- Built with **Python 3.11+**
- Inspired by real-world academic management systems
- Thanks to all contributors and users


### Quick Start Guide

```bash
# Clone and setup
git clone <your-repo-url>
cd student_course_management
python main.py


## Contact

For questions or feedback, please contact [ishimwediane400@gmail.com]

## demo video(screen recording)
 - https://drive.google.com/file/d/1Z6IDKblpJaY4GK0eY42cLaYaffbqA0zU/view?usp=sharing