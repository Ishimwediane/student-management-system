from models.student import Student, Undergraduate, Graduate
from models.course import Course
from models.enums import Level, FieldOfStudy


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
            print(f"avaibale levels:{[lvl.value for lvl in Level]}")
            level = input("Level : ").strip().lower()
            
            try:
                level_enum=Level(level)
            except ValueError:
                print(f"invalid level '{level}'.Must be one of {[lvl.value for lvl in Level]}")
                continue
                
            print(f"avaibale fields:{[field.value for field in FieldOfStudy]}")
            field_of_study = input("Field of study: ").strip().lower()
            
            try:
                field_enum=FieldOfStudy(field_of_study)
            except ValueError:
                print(f"invalid field '{field_of_study}'.Must be one of {[field.value for field in FieldOfStudy]}")
                continue          
            

            try:
                if level_enum == Level.UNDERGRADUATE:
                    student = Undergraduate(name, student_id, gender, email, field_of_study)
                else:
                    student = Graduate(name, student_id, gender, email, field_of_study)         

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
                
                print(f"available levels:{[lvl.value for lvl in Level]}")
                level=input("allowed levels(comma separated,blank:all):").strip()
                
                try:
                    level_enum=Level(level)
                except ValueError:
                    print(f"invalid level input")
                    continue                    
                
                
                print(f"available fields:{[field.value for field in FieldOfStudy]}")
                field=input("allowed fields(comma separated,blank:all):").strip()
                
                try:
                    field_enum=FieldOfStudy(field)
                except ValueError:
                    print(f"invalid field input")
                    continue

                
                

                course = Course(title, course_id, field_enum,level_enum)
                courses[course_id] = course
                print(f"Course added: {course.title} ({course.course_id})")
                print(f"Allowed Levels: {[lvl.value for lvl in course.allowed_levels]}")
                print(f"Allowed Fields: {[lvl.value for lvl in course.allowed_fields]}")

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