# Student Course Management System

A **console-based Python application** to manage students, courses, enrollments, and grades.  
This project demonstrates **Python fundamentals**, **OOP principles**, **modular programming**, and **data handling** in a simple CLI environment.

---

## Features

- Add **Undergraduate** or **Graduate** students with email and field of study  
- Add **courses** with unique IDs  
- Enroll students in one or more courses  
- Set **grades** for students per course (0–100)  
- Calculate **total average grades** per student  
- Show **student transcripts** including academic status:
  - First Class, Second Upper, Second Lower, Pass, Fail  
- List all students in a course with their grades  
- Update course titles  
- Remove students from courses  
- List all courses and all students  
- Simple **Command-Line Interface (CLI)**  

---

## Project Structure

```
student_course_management/
│
├─ models/
│  ├─ __init__.py
│  ├─ student.py          # Contains Student, Undergraduate, Graduate classes
│  └─ course.py           # Contains Course class
│
├─ main.py                # CLI application to interact with students and courses
├─ requirements.txt       # Python version and optional packages
└─ README.md
```

---

## Setup Instructions

1. **Install Python 3.11+**  
   Check installation:  
   ```bash
   python --version
   ```

2. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd student_course_management
   ```

3. **Install dependencies (if any)**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## Requirements

- **Python 3.11 or higher**
- Optional packages for future enhancements:
  ```txt
  tabulate==0.9.0   # Pretty CLI tables
  pandas==2.1.0     # Export data to CSV/Excel
  ```

---

## Usage

- **Add Students**: Provide name, ID, gender, email, level, and field of study.
- **Add Courses**: Provide course title and unique course ID.
- **Enroll Students**: Students can enroll in multiple courses.
- **Set Grades**: Assign grades per course (0–100).
- **View Transcript**: Shows all courses, grades, total average, and academic status.
- **List Students in a Course**: Displays enrolled students and their grades.
- **Update Course**: Change the course title.
- **Remove Student**: Remove a student from a specific course.

---

## Example Output

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

Select an option: 1

Name: Alice
Student ID: U123
Gender (male/female): female
Email: alice@gmail.com
Level (undergraduate/graduate): undergraduate
Field of study: Computer Science

✔ Student added: Alice undergraduate in Computer Science
```

---

## Demo

A Loom video demonstrates:
- Adding students
- Creating courses
- Enrolling students
- Setting grades
- Generating transcripts and reports

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or feedback, please contact [ishimwediane400@gmail.com]