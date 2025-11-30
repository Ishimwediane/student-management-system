from models.student import Undergraduate, Graduate
from models.course import Course
from models.enums import Level, FieldOfStudy


def add_student(students: dict):
    name = input("Name: ").strip()
    student_id = input("Student ID: ").strip()

    if student_id in students:
        print("Student ID already exists!")
        return

    gender = input("Gender (male/female): ").strip()
    email = input("Email: ").strip()

    print(f"Available Levels: {[lvl.value for lvl in Level]}")
    level_input = input("Level: ").strip().lower()

    try:
        level_enum = Level(level_input)
    except ValueError:
        print(f"Invalid level '{level_input}'.")
        return

    print(f"Available Fields: {[f.value for f in FieldOfStudy]}")
    field_input = input("Field of study: ").strip().lower()

    try:
        field_enum = FieldOfStudy(field_input)
    except ValueError:
        print(f"Invalid field '{field_input}'.")
        return

    if level_enum == Level.UNDERGRADUATE:
        student = Undergraduate(name, student_id, gender, email, field_enum)
    else:
        student = Graduate(name, student_id, gender, email, field_enum)

    students[student_id] = student
    print(f"✅ Student added: {student.name} ({student.level.value})")


def add_course(courses: dict):
    title = input("Course title: ").strip()
    course_id = input("Course ID: ").strip()

    if course_id in courses:
        print("Course ID already exists!")
        return

    print(f"Available Levels: {[lvl.value for lvl in Level]}")
    level_input = input("Allowed Level: ").strip().lower()

    try:
        allowed_level = Level(level_input)
    except ValueError:
        print("Invalid level.")
        return

    print(f"Available Fields: {[f.value for f in FieldOfStudy]}")
    field_input = input("Allowed Field: ").strip().lower()

    try:
        allowed_field = FieldOfStudy(field_input)
    except ValueError:
        print("Invalid field.")
        return

    course = Course(title, course_id, [allowed_field], [allowed_level])
    courses[course_id] = course

    print(f"✅ Course added: {course.title} ({course.course_id})")


def enroll_student(students, courses):
    sid = input("Student ID: ").strip()
    cid = input("Course ID: ").strip()

    student = students.get(sid)
    course = courses.get(cid)

    if student and course:
        course.enroll(student)
    else:
        print("Student or Course not found.")


def set_grade(students, courses):
    sid = input("Student ID: ").strip()
    cid = input("Course ID: ").strip()

    try:
        grade = float(input("Grade (0-100): ").strip())
    except ValueError:
        print("Invalid grade.")
        return

    student = students.get(sid)
    course = courses.get(cid)

    if student and course:
        course.set_grade(student, grade)
    else:
        print("Student or Course not found.")


def list_students_in_course(courses):
    cid = input("Course ID: ").strip()
    course = courses.get(cid)

    if course:
        course.list_students()
    else:
        print("Course not found.")


def show_transcript(students):
    sid = input("Student ID: ").strip()
    student = students.get(sid)

    if student:
        student.transcript()
    else:
        print("Student not found.")


def update_course(courses):
    cid = input("Course ID to update: ").strip()
    course = courses.get(cid)

    if course:
        new_title = input("New Title (blank: skip): ").strip()
        if new_title:
            course.update_course(title=new_title)
    else:
        print("Course not found.")


def remove_student_from_course(students, courses):
    sid = input("Student ID: ").strip()
    cid = input("Course ID: ").strip()

    student = students.get(sid)
    course = courses.get(cid)

    if student and course:
        course.remove_student(student)
    else:
        print("Student or Course not found.")


def list_all_courses(courses):
    if not courses:
        print("No courses available.")
    else:
        for c in courses.values():
            print(f"{c.course_id} - {c.title}")


def list_all_students(students):
    if not students:
        print("No students found.")
    else:
        for s in students.values():
            print(f"{s.student_id}: {s.name} | {s.level.value} | {s.field_of_studies.value}")


def run_cli():
    students = {}
    courses = {}

    while True:
        print("\n--- Student Course Management System ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Set Grade for Student in Course")
        print("5. List Students in a Course")
        print("6. Show Student Transcript")
        print("7. Update Course")
        print("8. Remove Student from Course")
        print("9. List All Courses")
        print("10. List All Students")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            add_course(courses)

        elif choice == "3":
            enroll_student(students, courses)

        elif choice == "4":
            set_grade(students, courses)

        elif choice == "5":
            list_students_in_course(courses)

        elif choice == "6":
            show_transcript(students)

        elif choice == "7":
            update_course(courses)

        elif choice == "8":
            remove_student_from_course(students, courses)

        elif choice == "9":
            list_all_courses(courses)

        elif choice == "10":
            list_all_students(students)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")
