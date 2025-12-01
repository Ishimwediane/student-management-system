from models.student import Undergraduate, Graduate
from models.course import Course
from models.enums import Level, FieldOfStudy

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

    print(f"Course added: {course.title} ({course.course_id})")

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

