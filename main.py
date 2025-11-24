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
        print("4. Set Grade for Student in Course")
        print("5. List Students in a Course")
        print("6. Show Student Transcript")
        print("7. Update Course")
        print("8. Remove Student from Course")
        print("9. List All Courses")
        print("10. List All Students")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            # Add student
            name = input("Name: ").strip()
            student_id = input("Student ID: ").strip()
            gender = input("Gender (male/female): ").strip()
            email = input("Email: ").strip()
            level = input("Level (undergraduate/graduate): ").strip().lower()
            field_of_study = input("Field of study: ").strip()

            try:
                if level.startswith("undergrad"):
                    student = Undergraduate(name, student_id, gender, email, field_of_study)
                else:
                    student = Graduate(name, student_id, gender, email, field_of_study)
                # Using setters ensures validation
                student.name = name
                student.gender = gender
                student.email = email
                students.append(student)
                print(f"✔ Student added: {student}")
            except ValueError as e:
                print(f"⚠ Error adding student: {e}")

        elif choice == "2":
            # Add course
            title = input("Course title: ").strip()
            course_id = input("Course ID: ").strip()
            try:
                course = Course(title, course_id)
                course.title = title  # validation via setter
                courses.append(course)
                print(f"✔ Course added: {course.title} ({course.course_id})")
            except ValueError as e:
                print(f"⚠ Error adding course: {e}")

        elif choice == "3":
            # Enroll student in course
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()

            student_list = [s for s in students if s.student_id == sid]
            course_list = [c for c in courses if c.course_id == cid]

            student = student_list[0] if student_list else None
            course = course_list[0] if course_list else None

            if student and course:
                course.enroll(student)
            else:
                print("⚠ Student or Course not found.")

        elif choice == "4":
            # Set grade for student in course
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            grade_input = input("Grade (0-100): ").strip()

            try:
                grade = float(grade_input)
            except ValueError:
                print("⚠ Invalid grade input.")
                continue

            student_list = [s for s in students if s.student_id == sid]
            course_list = [c for c in courses if c.course_id == cid]

            student = student_list[0] if student_list else None
            course = course_list[0] if course_list else None

            if student and course:
                try:
                    course.set_grade(student, grade)
                except ValueError as e:
                    print(f"⚠ {e}")
            else:
                print("⚠ Student or Course not found.")

        elif choice == "5":
            # List students in a course
            cid = input("Course ID: ").strip()
            course_list = [c for c in courses if c.course_id == cid]
            course = course_list[0] if course_list else None

            if course:
                course.list_students()
            else:
                print("⚠ Course not found.")

        elif choice == "6":
            # Show student transcript
            sid = input("Student ID: ").strip()
            student_list = [s for s in students if s.student_id == sid]
            student = student_list[0] if student_list else None

            if student:
                student.transcript()
            else:
                print("⚠ Student not found.")

        elif choice == "7":
            # Update course
            cid = input("Course ID to update: ").strip()
            course_list = [c for c in courses if c.course_id == cid]
            course = course_list[0] if course_list else None

            if course:
                new_title = input("New title (leave blank to skip): ").strip()
                kwargs = {}
                if new_title:
                    kwargs["title"] = new_title
                course.update_course(**kwargs)
            else:
                print("⚠ Course not found.")

        elif choice == "8":
            # Remove student from course
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()

            student_list = [s for s in students if s.student_id == sid]
            course_list = [c for c in courses if c.course_id == cid]

            student = student_list[0] if student_list else None
            course = course_list[0] if course_list else None

            if student and course:
                course.remove_student(student)
            else:
                print("⚠ Student or Course not found.")

        elif choice == "9":
            # List all courses
            if not courses:
                print("No courses available.")
            else:
                for c in courses:
                    print(f"{c.course_id}: {c.title}")

        elif choice == "10":
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
            print("⚠ Invalid option. Try again.")


if __name__ == "__main__":
    main()
