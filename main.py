# main.py
from models.student import Student, Undergraduate, Graduate
from models.course import Course

def main():
    students = []
    courses = []

    while True:
        print("\n--- Student Course Management System ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. List Students in a Course")
        print("5. Update Course")
        print("6. Remove Student from Course")
        print("7. List All Courses")
        print("8. List All Students")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            # Add student
            name = input("Name: ")
            sid = input("Student ID: ")
            gender = input("Gender (male/female): ")
            level = input("Level (undergraduate/graduate): ").lower()
            field = input("Field of study: ")

            if level == "undergraduate":
                student = Undergraduate(name, sid, field)
            else:
                student = Graduate(name, sid, field)
            student.gender = gender  # validate gender
            students.append(student)
            print(f"✔ Student added: {student}")

        elif choice == "2":
            # Add course
            title = input("Course title: ")
            cid = input("Course ID: ")
            course = Course(title, cid)
            courses.append(course)
            print(f"✔ Course added: {course.title} ({course.course_id})")

        elif choice == "3":
            # Enroll student
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            student = next((s for s in students if s.student_id == sid), None)
            course = next((c for c in courses if c.course_id == cid), None)
            if student and course:
                course.enroll(student)
            else:
                print("⚠ Student or Course not found.")

        elif choice == "4":
            # List students in a course
            cid = input("Course ID: ")
            course = next((c for c in courses if c.course_id == cid), None)
            if course:
                print(f"Students in {course.title}:")
                course.list_students()
            else:
                print("⚠ Course not found.")

        elif choice == "5":
            # Update course
            cid = input("Course ID to update: ")
            course = next((c for c in courses if c.course_id == cid), None)
            if course:
                new_title = input("New title (leave blank to skip): ").strip()
                kwargs = {}
                if new_title:
                    kwargs["title"] = new_title
                course.update_course(**kwargs)
            else:
                print("⚠ Course not found.")

        elif choice == "6":
            # Remove student from course
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            student = next((s for s in students if s.student_id == sid), None)
            course = next((c for c in courses if c.course_id == cid), None)
            if student and course:
                course.remove_student(student)
            else:
                print("⚠ Student or Course not found.")

        elif choice == "7":
            # List all courses
            if not courses:
                print("No courses available.")
            else:
                for c in courses:
                    print(f"{c.course_id}: {c.title}")

        elif choice == "8":
            # List all students
            if not students:
                print("No students available.")
            else:
                for s in students:
                    print(s)

        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
