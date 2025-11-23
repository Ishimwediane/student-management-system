from student import Student

class Course:
    def __init__(self, title, course_id):
        self._course_id = course_id
        self._title = title
        self.enrolled_students = []

    @property
    def course_id(self):
        return self._course_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not new_title or not new_title.strip():
            raise ValueError("Course title is required")
        self._title = new_title

    # Enroll student
    def enroll(self, student: Student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            student.course_grades[self.course_id] = None
            print(f"{student.name} enrolled in {self.title}")
        else:
            print(f"{student.name} is already enrolled in {self.title}")

    # Remove student
    def remove_student(self, student: Student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.course_grades.pop(self.course_id, None)
            print(f"{student.name} removed from {self.title}")
        else:
            print(f"{student.name} is not enrolled in {self.title}")

    # Set grade
    def set_grade(self, student: Student, grade):
        if student not in self.enrolled_students:
            print(f"{student.name} is not enrolled in {self.title}")
            return
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        student.course_grades[self.course_id] = grade
        print(f"Set grade {grade} for {student.name} in {self.title}")

    # Course average
    def average_grade(self):
        grades = [
            student.course_grades[self.course_id]
            for student in self.enrolled_students
            if student.course_grades[self.course_id] is not None
        ]
        if not grades:
            return 0
        return sum(grades) / len(grades)

    # List students
    def list_students(self):
        print(f"\nStudents enrolled in {self.title}:")
        if not self.enrolled_students:
            print("No students yet.")
            return
        for student in self.enrolled_students:
            grade = student.course_grades[self.course_id]
            grade_display = grade if grade is not None else "Not yet graded"
            print(f"{student.name} - Grade: {grade_display}")

    # Update course title
    def update_course(self, **kwargs):
        for key, value in kwargs.items():
            attribute_name = f"_{key}"
            if hasattr(self, attribute_name):
                setattr(self, attribute_name, value)
            else:
                print(f"Attribute '{key}' does not exist in Course")
        print(f"Course {self.course_id} updated successfully")

    def __str__(self):
        return f"{self.title} ({self.course_id}) - {len(self.enrolled_students)} students"
