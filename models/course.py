from abc import ABC, abstractmethod
from .student import Student
from .enrollment import Enrollment

class Course:
    def __init__(self, title, course_id, allowed_levels=None, allowed_fields=None):
        self._title = title
        self._course_id = course_id
        self.enrollments = []
        self.allowed_levels = allowed_levels if allowed_levels else ["undergraduate", "graduate"]
        self.allowed_fields = allowed_fields if allowed_fields else "all"

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Course title is required")
        self._title = value

    @property
    def course_id(self):
        return self._course_id
    
    @property
    def allowed_fields(self):
        return self._allowed_levels

    @allowed_levels.setter
    def allowed_levels(self, value):
        if not value.replace(" ", "").isalpha():
           raise ValueError("Name can only contain letters and spaces")
        self._allowed_levels = value



    def enroll(self, student: Student):
        if student.level not in self.allowed_levels:
            print(f"{student.name} cannot enroll: level not allowed")
            return
        if self.allowed_fields != "all" and student.field_of_studies not in self.allowed_fields:
            print(f"{student.name} cannot enroll: field not allowed")
            return
        if any(en.student == student for en in self.enrollments):
            print(f"{student.name} already enrolled")
            return
        enrollment = Enrollment(student)
        self.enrollments.append(enrollment)
        student.course_grades[self.course_id] = None
        print(f"{student.name} enrolled in {self.title}")

    def remove_student(self, student: Student):
        for en in self.enrollments:
            if en.student == student:
                self.enrollments.remove(en)
                student.course_grades.pop(self.course_id, None)
                print(f"{student.name} removed from {self.title}")
                return
        print(f"{student.name} not enrolled in {self.title}")

    def set_grade(self, student: Student, grade):
        enrollment = next((en for en in self.enrollments if en.student == student), None)
        if not enrollment:
            print(f"{student.name} not enrolled in {self.title}")
            return
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be 0-100")
        enrollment.grade = grade
        student.course_grades[self.course_id] = grade
        print(f"Grade {grade} set for {student.name} in {self.title}")

    def average_grade(self):
        grades = [en.grade for en in self.enrollments if en.grade is not None]
        return sum(grades) / len(grades) if grades else 0

    def list_students(self):
        print(f"\nStudents in {self.title}:")
        if not self.enrollments:
            print("No students yet")
            return
        for en in self.enrollments:
            print(en)

    def update_course(self, **kwargs):
        for key, value in kwargs.items():
            attr = f"_{key}"
            if hasattr(self, attr):
                setattr(self, attr, value)
            else:
                print(f"Attribute '{key}' not found")
        print(f"Course {self.course_id} updated")

    def __str__(self):
        return f"{self.title} ({self.course_id}) - {len(self.enrollments)} students"
