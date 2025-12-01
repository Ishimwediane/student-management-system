from models.student import Undergraduate, Graduate
from models.course import Course
from models.enums import Level, FieldOfStudy

def enroll_student(students, courses):
    sid = input("Student ID: ").strip()
    cid = input("Course ID: ").strip()

    student = students.get(sid)
    course = courses.get(cid)

    if student and course:
        course.enroll(student)
    else:
        print("Student or Course not found.")

