class Student:
    def __init__(self,name,student_id,gender,level="undergraduale"):
        self._name=name
        self.student_id=student_id
        self._gender=gender.lower()
        self.level=level
        
    @property
    def name(self):
        return self._name
    
    @property
    def gender(self):
        return self._gender
    

    @name.setter
    def name(self, value):
        if not value.strip():  
            raise ValueError("Name cannot be empty")
        self._name = value
        
    @gender.setter
    def gender(self,value):
        if value.lovwer() not in ("male","female"):
            raise ValueError("gender must be male or female")
        self._gender=value.lower()
    
    def __str__(self):
        return f"{self.name}with{self.student_id} and {self.gender} is in {self.level}"
    
    def __str__(self):
        """String representation for UI/printing."""
        return f"{self.name} ({self.level})"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Student(student_id='{self.student_id}', name='{self.name}')"

    def __eq__(self, other):
        """Compare students by ID."""
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False
    
class Undergraduate(Student):
    def __init__(self,name,student_id,field_of_studies):
        super().__init__(name,student_id,level="undergraduate")
        self.field_of_studies=field_of_studies
    
    def __str__(self):
        return f"{self.name} undegraduate in {self.field_of_studies}"

class Graduate(Student):
    def __init__(self,name,student_id,field_of_studies):
        super().__init__(name,student_id,level="graduate")
        self.field_of_studies=field_of_studies
    
    def __str__(self):
        return f"{self.name} graduate in {self.field_of_studies}"

