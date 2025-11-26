from abc import ABC, abstractmethod

class Student(ABC):
    """
    Abstract Base Class for a Student
    """
    def __init__(self, name, student_id, gender, email, level="undergraduate"):
        self._name = name
        self.student_id = student_id
        self.gender = gender
        self.email = email
        self.level = level
        self.course_grades = {}

    # Name
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name can only contain letters and spaces")
        self.name = value

    # Gender
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, value):
        value = value.lower()
        if value not in ("male", "female"):
            raise ValueError("Gender must be male or female")
        self._gender = value

    # Email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email")
        self._email = value

    # Student ID
    @property
    def student_id(self):
        return self._student_id
    @student_id.setter
    def student_id(self, value):
        if not value.strip():
            raise ValueError("Student ID cannot be empty")
        self._student_id = value

    # Level
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        value = value.lower()
        if value not in ("undergraduate", "graduate"):
            raise ValueError("Invalid level")
        self._level = value

    # Total average
    def total_average(self):
        grades = [g for g in self.course_grades.values() if g is not None]
        return sum(grades) / len(grades) if grades else 0

    @property
    def academic_status(self):
        avg = self.total_average()
        if avg >= 80:
            return "First Class"
        elif avg >= 70:
            return "Second Upper Class"
        elif avg >= 60:
            return "Second Lower Class"
        elif avg >= 50:
            return "Pass"
        else:
            return "Fail"
        
    #Transcript
    def transcript(self):
        print(f"\nTranscript - {self.name} ({self.student_id})")
        print("-" * 45)
        if not self.course_grades:
            print("No courses enrolled.")
        else:
            for course_id, grade in self.course_grades.items():
                print(f"{course_id}: {grade if grade is not None else 'Not yet graded'}")
        print("-" * 45)
        print(f"Total Average: {self.total_average():.2f}")
        print(f"Academic Status: {self.academic_status}")

    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.level}"
    def __repr__(self):
        return f"Student(student_id='{self.student_id}', name='{self.name}')"
    def __eq__(self, other):
        return isinstance(other, Student) and self.student_id == other.student_id

# Subclasses
class Undergraduate(Student):
    def __init__(self, name, student_id, gender, email, field_of_studies):
        super().__init__(name, student_id, gender, email, level="undergraduate")
        self.field_of_studies = field_of_studies
        
    @property
    def field_of_studies(self):
        return self._field_of_studies
    
    @field_of_studies.setter
    def field_of_studies(self, value):
        if not value.replace(" ", "").isalpha():
           raise ValueError("Name can only contain letters and spaces")
        self._field_of_studies = value

    def __str__(self):
        return f"{self.name} - Undergraduate in {self.field_of_studies}"

class Graduate(Student):
    def __init__(self, name, student_id, gender, email, field_of_studies):
        super().__init__(name, student_id, gender, email, level="graduate")
        self.field_of_studies = field_of_studies
        
    @property
    def field_of_studies(self):
        return self._field_of_studies
    
    @field_of_studies.setter
    def field_of_studies(self, value):
        if not value.replace(" ", "").isalpha():
           raise ValueError("Name can only contain letters and spaces")
        self._field_of_studies = value

    def __str__(self):
        return f"{self.name} - Graduate in {self.field_of_studies}"
