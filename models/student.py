class Student:
    def __init__(self,name,student_id,gender,level="undergraduale"):
        self.name=name
        self.student_id=student_id
        self.gender=gender
        self.level=level
        
    
    def __str__(self):
        return f"{self.name}with{self.student_id} and {self.gender} is in {self.level}"
    
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

