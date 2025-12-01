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
    print(f"Student added: {student.name} ({student.level.value})")

def show_transcript(students):
    sid = input("Student ID: ").strip()
    student = students.get(sid)

    if student:
        student.transcript()
    else:
        print("Student not found.")


def list_all_students(students):
    if not students:
        print("No students found.")
    else:
        for s in students.values():
            print(f"{s.student_id}: {s.name} | {s.level.value} | {s.field_of_studies.value}")

