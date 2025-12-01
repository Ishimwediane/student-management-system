from .course import Course
from .student import Student

def full_transcript(student: Student, courses: list[Course]):
    """
    Prints full transcript of a student across all courses.
    """
    print(f"\nFull Transcript for {student.name}:")
    total, count = 0, 0
    for course in courses:
        enrollment = next((en for en in course.enrollments if en.student == student), None)
        if enrollment:
            grade = enrollment.grade
            grade_display = grade if grade is not None else "Not graded"
            print(f"{course.title}: {grade_display}")
            if grade is not None:
                total += grade
                count += 1
    avg = total / count if count else 0
    print(f"Total Average: {avg:.2f}")
    print(f"Academic Status: {Student.get_academic_status(avg)}\n")
