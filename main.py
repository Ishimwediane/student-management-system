from models.student import Student,Undergraduate,Graduate
from models.course import Course

def main():
    students=[]
    courses=[]
    
    while True:
        print("---Student Course Management System---")
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
        
        choice = input("Select an optiom").strip()
        
        if choice =="1":
            name = input("Name: ").strip()
            sid = input("Student ID: ").strip()
            gender = input("Gender (male/female): ").strip().lower()
            email = input("Email: ").strip()
            level = input("Level (undergraduate/graduate): ").strip().lower()
            field = input("Field of study: ").strip()
            
            try:
                if level == "undergraduate":
                    student = Undergraduate(name, sid, gender, email, field)
                else:
                    student = Graduate(name, sid, gender, email, field)
                students.append(student)
                print(f"Student added: {student}")
            except ValueError as e:
                print(f" Error: {e}")
                
        
        elif choice == "2":
            title = input("Course title: ").strip()
            cid = input("Course ID: ").strip()
            try:
                course = Course(title, cid)
                courses.append(course)
                print(f"Course added: {course.title} ({course.course_id})")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            student = next((s for s in students if s.student_id == sid), None)
            course = next((c for c in courses if c.course_id == cid), None)
            if student and course:
                course.enroll(student)
            else:
                print("Student or Course not found.")

        elif choice == "4":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            try:
                grade = float(input("Grade (0-100): ").strip())
            except ValueError:
                print("Grade must be a number.")
                continue

            student = next((s for s in students if s.student_id == sid), None)
            course = next((c for c in courses if c.course_id == cid), None)
            if student and course:
                try:
                    course.set_grade(student, grade)
                except ValueError as e:
                    print(f" {e}")
            else:
                print("Student or Course not found.")

        elif choice == "5":
            cid = input("Course ID: ").strip()
            course = next((c for c in courses if c.course_id == cid), None)
            if course:
                course.list_students()
            else:
                print("Course not found.")

        elif choice == "6":
            sid = input("Student ID: ").strip()
            student = next((s for s in students if s.student_id == sid), None)
            if student:
                student.transcript()
            else:
                print(" Student not found.")

        elif choice == "7":
            
            cid = input("Course ID to update: ").strip()
            course = next((c for c in courses if c.course_id == cid), None)
            if course:
                new_title = input("New title (leave blank to skip): ").strip()
                if new_title:
                    course.update_course(title=new_title)
                else:
                    print("No changes made.")
            else:
                print("Course not found.")

        elif choice == "8":
            
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            student = next((s for s in students if s.student_id == sid), None)
            course = next((c for c in courses if c.course_id == cid), None)
            if student and course:
                course.remove_student(student)
            else:
                print(" Student or Course not found.")

        elif choice == "9":
           
            if not courses:
                print("No courses available.")
            else:
                for c in courses:
                    print(f"{c.course_id}: {c.title} ({len(c.enrolled_students)} students)")

        elif choice == "10":
        
            if not students:
                print("No students available.")
            else:
                for s in students:
                    print(f"{s} - Email: {s.email}")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()