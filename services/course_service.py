from models.course import Course
from models.enums import Level, FieldOfStudy
from models.student import Student

class CourseService:
    @staticmethod
    def add_course(courses: dict, title, course_id, allowed_field, allowed_level):
        if course_id in courses:
            raise ValueError("Course ID already exists")
        course = Course(title, course_id, [FieldOfStudy(allowed_field)], [Level(allowed_level)])
        courses[course_id] = course
        return course

    @staticmethod
    def get_course(courses: dict, course_id: str):
        return courses.get(course_id)

    @staticmethod
    def list_students(course: Course):
        return course.enrollments
