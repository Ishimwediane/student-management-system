from .student import Student

class Enrollment:
    """
    Represents the enrollment of a student in a course, along with their grade.
    """
    def __init__(self, student: Student):
        self.student = student
        self.grade = None

    def __str__(self):
        grade_display = self.grade if self.grade is not None else "Not graded"
        return f"{self.student.name} ({self.student.field_of_studies.value}) - Grade: {grade_display}"
