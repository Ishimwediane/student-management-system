from models.course import Course
from models.enums import Level, FieldOfStudy

def add_course(courses: dict):
    title = input("Course title: ").strip()
    course_id = input("Course ID: ").strip()
    if course_id in courses:
        print("Course ID already exists!")
        return

    print(f"Available levels: {[lvl.value for lvl in Level]}")
    level_input = input("Allowed level: ").strip().lower()
    try:
        level_enum = Level(level_input)
    except ValueError:
        print("Invalid level.")
        return

    print(f"Available fields: {[f.value for f in FieldOfStudy]}")
    field_input = input("Allowed field: ").strip().lower()
    try:
        field_enum = FieldOfStudy(field_input)
    except ValueError:
        print("Invalid field.")
        return

    course = Course(title, course_id, [field_enum], [level_enum])
    courses[course_id] = course
    print(f"Course added: {course.title}")

def get_course(courses: dict, course_id: str):
    return courses.get(course_id)