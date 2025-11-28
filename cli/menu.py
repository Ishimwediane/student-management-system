from models.student import Undergraduate, Graduate
from models.course import Course
from models.enums import Level, FieldOfStudy


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

        # add student
        if choice == "1":
            name = input("Name: ").strip()
            student_id = input("Student ID: ").strip()

            if student_id in students:
                print("Student ID already exists!")
                continue

            gender = input("Gender (male/female): ").strip()
            email = input("Email: ").strip()

            print(f"Available Levels: {[lvl.value for lvl in Level]}")
            level_input = input("Level: ").strip().lower()

            try:
                level_enum = Level(level_input)
            except ValueError:
                print(f"Invalid level '{level_input}'. Must be {[lvl.value for lvl in Level]}")
                continue

            print(f"Available Fields: {[f.value for f in FieldOfStudy]}")
            field_input = input("Field of study: ").strip().lower()

            try:
                field_enum = FieldOfStudy(field_input)
            except ValueError:
                print(f"Invalid field '{field_input}'. Must be {[f.value for f in FieldOfStudy]}")
                continue

            try:
                if level_enum == Level.UNDERGRADUATE:
                    student = Undergraduate(name, student_id, gender, email, field_enum)
                else:
                    student = Graduate(name, student_id, gender, email, field_enum)

                students[student_id] = student
                print(f"Student added: {student.name} ({student.level.value})")

            except ValueError as e:
                print(f"Error adding student: {e}")

        # ADD COURSE 
        elif choice == "2":
            try:
                title = input("Course title: ").strip()
                course_id = input("Course ID: ").strip()

                if course_id in courses:
                    print("Course ID already exists!")
                    continue

                print(f"Available Levels: {[lvl.value for lvl in Level]}")
                level_input = input("Allowed Level: ").strip().lower()

                try:
                    allowed_level = Level(level_input)
                except ValueError:
                    print("Invalid level.")
                    continue

                print(f"Available Fields: {[f.value for f in FieldOfStudy]}")
                field_input = input("Allowed Field: ").strip().lower()

                try:
                    allowed_field = FieldOfStudy(field_input)
                except ValueError:
                    print("Invalid field.")
                    continue

               
                course = Course(title, course_id, [allowed_field], [allowed_level])
                courses[course_id] = course

                print(f"Course added: {course.title} ({course.course_id})")

            except ValueError as e:
                print(f"Error adding course: {e}")

        # ENROLL STUDENT 
        elif choice == "3":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()

            student = students.get(sid)
            course = courses.get(cid)

            if student and course:
                course.enroll(student)
            else:
                print("Student or Course not found.")

        # SET GRADE 
        elif choice == "4":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            grade_input = input("Grade (0-100): ").strip()

            try:
                grade = float(grade_input)
            except ValueError:
                print("Invalid grade.")
                continue

            student = students.get(sid)
            course = courses.get(cid)

            if student and course:
                try:
                    course.set_grade(student, grade)
                except ValueError as e:
                    print(e)
            else:
                print("Student or Course not found.")

        #  LIST STUDENTS IN COURSE 
        elif choice == "5":
            cid = input("Course ID: ").strip()
            course = courses.get(cid)
            if course:
                course.list_students()
            else:
                print("Course not found.")

        # STUDENT TRANSCRIPT 
        elif choice == "6":
            sid = input("Student ID: ").strip()
            student = students.get(sid)
            if student:
                student.transcript()
            else:
                print("Student not found.")

        # UPDATE COURSE
        elif choice == "7":
            cid = input("Course ID to update: ").strip()
            course = courses.get(cid)

            if course:
                new_title = input("New Title (blank: skip): ").strip()
                if new_title:
                    course.update_course(title=new_title)
            else:
                print("Course not found.")

        #  REMOVE STUDENT 
        elif choice == "8":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()

            student = students.get(sid)
            course = courses.get(cid)

            if student and course:
                course.remove_student(student)
            else:
                print("Student or Course not found.")

        #  LIST ALL COURSES 
        elif choice == "9":
            if not courses:
                print("No courses available.")
            else:
                for c in courses.values():
                    print(f"{c.course_id} - {c.title}")

        # LIST ALL STUDENTS 
        elif choice == "10":
            if not students:
                print("No students found.")
            else:
                print("\nAll Students:")
                for s in students.values():
                    print(f"{s.student_id}: {s.name} | {s.level.value} | {s.field_of_studies.value}")

        #  EXIT 
        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")