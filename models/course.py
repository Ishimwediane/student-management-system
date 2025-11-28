from abc import ABC, abstractmethod
from .student import Student
from .enrollment import Enrollment
from .enums import Level, FieldOfStudy

class Course:
    def __init__(self, title, course_id, allowed_levels=None, allowed_fields=None):
        self._title = title
        self._course_id = course_id
        self.enrollments = []
        self._allowed_levels = allowed_levels 
        self._allowed_fields = allowed_fields 

    # Title property 
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Course title is required")
        if not value.replace(" ", "").isalpha():
            raise ValueError("Course title can only contain letters and spaces")
        self._title = value

    # Course 
    @property
    def course_id(self):
        return self._course_id

    # Allowed Levels
    @property
    def allowed_levels(self):
        return self._allowed_levels

    @allowed_levels.setter
    def allowed_levels(self, value):
        if isinstance(value, list) and all(isinstance(v, str) and v.replace(" ", "").isalpha() for v in value):
            self._allowed_levels = value
        else:
            raise ValueError("allowed_levels must be a list of strings containing letters only")

    #  Allowed Fields property 
    @property
    def allowed_fields(self):
        return self._allowed_fields

    @allowed_fields.setter
    def allowed_fields(self, value):
        # Can be a list of strings or "all"
        if value != "all" and (not isinstance(value, list) or not all(isinstance(v, str) for v in value)):
            raise ValueError("allowed_fields must be 'all' or a list of strings")
        self._allowed_fields = value

    # --- Enroll a student ---
    def enroll(self, student: Student):
        if student.level not in self.allowed_levels:
            print(f"{student.name} cannot enroll: level '{student.level}' not allowed")
            return
        if self.allowed_fields != "all" and student.field_of_studies not in self.allowed_fields:
            print(f"{student.name} cannot enroll: field '{student.field_of_studies}' not allowed")
            return
        if any(en.student == student for en in self.enrollments):
            print(f"{student.name} already enrolled")
            return
        enrollment = Enrollment(student)
        self.enrollments.append(enrollment)
        student.course_grades[self.course_id] = None
        print(f"{student.name} enrolled in {self.title}")

    # --- Remove a student ---
    def remove_student(self, student: Student):
        for en in self.enrollments:
            if en.student == student:
                self.enrollments.remove(en)
                student.course_grades.pop(self.course_id, None)
                print(f"{student.name} removed from {self.title}")
                return
        print(f"{student.name} not enrolled in {self.title}")

    # --- Set a grade ---
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

    # --- Calculate average grade ---
    def average_grade(self):
        grades = [en.grade for en in self.enrollments if en.grade is not None]
        return sum(grades) / len(grades) if grades else 0

    # --- List all students ---
    def list_students(self):
        print(f"\nStudents in {self.title}:")
        if not self.enrollments:
            print("No students yet")
            return
        for en in self.enrollments:
            print(en)

    # --- Update course attributes ---
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
