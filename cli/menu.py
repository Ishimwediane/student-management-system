from models.student import Undergraduate, Graduate
from models.course import Course
from models.enums import Level, FieldOfStudy
from menu.student_menu import add_student, show_transcript, list_all_students
from menu.course_menu import add_course, set_grade, list_students_in_course, update_course, remove_student_from_course, list_all_courses
from menu.enrollment_menu import enroll_student


def run_cli():
    students = {}
    courses = {}

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
            add_student(students)

        elif choice == "2":
            add_course(courses)

        elif choice == "3":
            enroll_student(students, courses)

        elif choice == "4":
            set_grade(students, courses)

        elif choice == "5":
            list_students_in_course(courses)

        elif choice == "6":
            show_transcript(students)

        elif choice == "7":
            update_course(courses)

        elif choice == "8":
            remove_student_from_course(students, courses)

        elif choice == "9":
            list_all_courses(courses)

        elif choice == "10":
            list_all_students(students)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")
