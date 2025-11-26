from models.student import Student, Undergraduate, Graduate
from models.course import Course

def main():
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
            name = input("Name: ").strip()
            student_id = input("Student ID: ").strip()

            if student_id in students:
                print("Student ID already exists!")
                continue

            gender = input("Gender (male/female): ").strip()
            email = input("Email: ").strip()
            level = input("Level (undergraduate/graduate): ").strip().lower()
            field_of_study = input("Field of study: ").strip()
           

            try:
                if level == "undergraduate":
                    student = Undergraduate(name, student_id, gender, email, field_of_study)
                elif level == "graduate":
                    student = Graduate(name, student_id, gender, email, field_of_study)
                else:
                    raise ValueError("Level must be 'undergraduate' or 'graduate'")
                
                if student.student_id in students:
                    print("Student ID already exists!")
                    continue
             

                students[student_id] = student     
                print(f"Student added: {student}")

            except ValueError as e:
                print(f"Error adding student: {e}")

        
        elif choice == "2":
            # Add Course
            try:
                title = input("Course title: ").strip()
                course_id = input("Course ID: ").strip()
                if course_id in courses:
                    print("Course ID already exists!")
                    continue

                allowed_levels_input = input("Allowed Levels (comma separated, leave blank for both): ").strip()
                if not allowed_levels_input:
                   allowed_levels = ["undergraduate", "graduate"]
                else:
                   allowed_levels = [lvl.strip().lower() for lvl in allowed_levels_input.split(",")]
    
                   for lvl in allowed_levels:
                       if lvl not in ("undergraduate", "graduate"):
                          print(f"Invalid level '{lvl}'! Only 'undergraduate' and 'graduate' allowed.")
                          allowed_levels = ["undergraduate", "graduate"]
                          break

                allowed_fields_input = input("Allowed Fields (comma separated, leave blank for all): ").strip()
                if not allowed_fields_input:
                   allowed_fields = "all"
                else:
                   allowed_fields = [field.strip() for field in allowed_fields_input.split(",")]



                course = Course(title, course_id, allowed_levels, allowed_fields)
                courses[course_id] = course
                print(f"Course added: {course.title} ({course.course_id})")
                print(f"Allowed Levels: {course.allowed_levels}")
                print(f"Allowed Fields: {course.allowed_fields}")

            except ValueError as e:
                print(f"Error adding course: {e}")

        elif choice == "3":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            student = students.get(sid)
            course = courses.get(cid)

            if student and course:
                course.enroll(student)
            else:
                print("Student or Course not found.")

        elif choice == "4":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            grade_input = input("Grade (0-100): ").strip()

            try:
                grade = float(grade_input)
            except ValueError:
                print("Invalid grade input.")
                continue

            student = students.get(sid)
            course = courses.get(cid)

            if student and course:
                try:
                    course.set_grade(student, grade)
                except ValueError as e:
                    print(f"{e}")
            else:
                print("Student or Course not found.")

        elif choice == "5":
            cid = input("Course ID: ").strip()
            course = courses.get(cid)
            if course:
                course.list_students()
            else:
                print("Course not found.")

        elif choice == "6":
            sid = input("Student ID: ").strip()
            student = students.get(sid)
            if student:
                student.transcript()
            else:
                print("Student not found.")

        elif choice == "7":
            cid = input("Course ID to update: ").strip()
            course = courses.get(cid)
            if course:
                new_title = input("New title (leave blank to skip): ").strip()
                kwargs = {}
                if new_title:
                    kwargs["title"] = new_title
                course.update_course(**kwargs)
            else:
                print("Course not found.")

        elif choice == "8":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            student = students.get(sid)
            course = courses.get(cid)
            if student and course:
                course.remove_student(student)
            else:
                print("Student or Course not found.")

        elif choice == "9":
            if not courses:
                print("No courses available.")
            else:
                for c in courses.values():
                    print(f"{c.course_id}: {c.title}")

        elif choice == "10":
            if not students:
                print("No students available.")
            else:
                print("\nList of all Students:")
                for s in students.values():
                    print(f"{s.student_id}: {s.name}|{s.level}|{s.gender}|{s.email}|{s.field_of_studies}")

        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()