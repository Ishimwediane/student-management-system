from models.student import Student, Undergraduate, Graduate
from models.enums import Level, FieldOfStudy

def add_student(students):
    name = input("Name: ").strip()
    student_id = input("Student ID: ").strip()
    if student_id in students:
        print("Student ID already exists!")
        return

    gender = input("Gender (male/female): ").strip()
    email = input("Email: ").strip()
    print(f"Available levels: {[lvl.value for lvl in Level]}")
    level_input = input("Level: ").strip().lower()
    try:
        level_enum = Level(level_input)
    except ValueError:
        print("Invalid level.")
        return

    print(f"Available fields: {[f.value for f in FieldOfStudy]}")
    field_input = input("Field of study: ").strip().lower()
    try:
        field_enum = FieldOfStudy(field_input)
    except ValueError:
        print("Invalid field.")
        return

    student = Undergraduate(name, student_id, gender, email, field_enum) if level_enum == Level.UNDERGRADUATE else Graduate(name, student_id, gender, email, field_enum)
    students[student_id] = student
    print(f"Student added: {student}")

def get_student(students: dict, student_id: str):
    return students.get(student_id)
