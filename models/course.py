from .student import Student

class Course:
    def __init__(self, title, course_id):
        self._course_id=course_id
        self._title = title
        self.enrolled_students = []
    
    @property
    def course_id(self):
        """read-only"""
        return self._course_id
    
    @property
    def title(self):
        
        return self._title
    
    @title.setter
    def title(self,new_title):
        if not new_title or not new_title.strip():
            raise ValueError("course title is required")
        self._title=new_title
        
    
    


    def enroll(self, student: Student):
        """enroll a student into the course"""
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"{student.name} enrolled in {self.title}")
        else:
            print(f"{student.name} is already enrolled in {self.title}")
            
    def remove_student(self,student: Student):
        """remove student in a given course"""
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"student {student.name} is removed in {self.title}")
        else:
            print(f"student {student.name} don't exist in this course")
    
    def update_course(self,**kwargs):
        """updating course"""
        for key,value in kwargs.items():
            attribute_name = f"_{key}"
            if hasattr(self,attribute_name):
                setattr(self,attribute_name,value)
            else:
                print(f"attribute '{key}' don't exist in course")
        print(f"course {self.course_id} updated sucessfully")
        
   


    def __str__(self):
        return f"{self.title} by {self.instructor} - {len(self.enrolled_students)} students"

    def list_students(self):
        if not self.enrolled_students:
            print("No students enrolled yet.")
        for s in self.enrolled_students:
            print(s)
