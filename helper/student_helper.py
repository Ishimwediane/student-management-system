from ..models.enrollment import Enrollment
from ..models.course import Course

def calculate_total_average(student,courses):
    """
    Calculates the total average of a student across all courses.
    """
    grades=[en.grade for course in courses for en in course.enrollments if en.student == student and en.grade is not None]
    
    return sum(grades)/len(grades) if grades else 0

def print_transcript(student, courses):
    """
    Prints the transcript of a student across all courses.
    """
    print(f"\nTranscript for {student.name}(student.student_id):")
    print("-"*45)
    student_enrollments=[en for course in courses for en in course.enrollments if en.student ==student]
    
    if not student_enrollments:
        print(f"{student.name} has not enrolled in any courses.")
    else:
        [print(f"{en.course.title}-{en.grade if en.grade is not None else 'Not graded'}") for en in student_enrollments]
    avg=calculate_total_average(student,courses)
    print("-"*45)
    print(f"Total Average: {avg:.2f}")
    print(f"Academic Status: {student.get_academic_status(avg)}\n")     
    