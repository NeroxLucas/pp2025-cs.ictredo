import curses
from curses import wrapper
from input import get_student_info, get_course_info, get_mark_info
from output import display_menu, display_message
from domains import Student
from domains import Course
from domains import Mark

StudentList = []
CourseList = []
MarkList = []
SortGPA = {}

def calculate_gpa(student_id):
    student_marks = [mark.mark for mark in MarkList if mark.StudentID == student_id]
    if student_marks:
        return round(sum(student_marks) / len(student_marks), 2)
    return None

def management(stdscr):
    curses.curs_set(0) #Hide cursor 
    while True:
        stdscr.clear()
        try:
            display_menu(stdscr) 
            choice = stdscr.getstr().decode("utf-8").strip()
            
            if choice == "1":  
                name, student_id = get_student_info(stdscr)
                StudentList.append(Student(name, student_id))
                display_message(stdscr, "Student added successfully!")
            
            elif choice == "2":  
                name, course_id = get_course_info(stdscr)
                CourseList.append(Course(name, course_id))
                display_message(stdscr, "Course added successfully!")
            
            elif choice == "3":  
                student_id, course_id, mark = get_mark_info(stdscr)
                MarkList.append(Mark(student_id, course_id, mark))
                display_message(stdscr, "Mark added successfully!")
            
            elif choice == "4":  
                stdscr.addstr("\nEnter student ID to calculate GPA: ")
                stdscr.refresh()
                student_id = int(stdscr.getstr().decode("utf-8").strip())
                gpa = calculate_gpa(student_id)
                if gpa is not None:
                    SortGPA[student_id] = gpa
                    display_message(stdscr, f"GPA for student {student_id}: {gpa}")
                else:
                    display_message(stdscr, "No marks found for this student.")
            
            elif choice == "5":  
                if not SortGPA:
                    display_message(stdscr, "No GPA data available to rank.")
                else:
                    sorted_gpa = sorted(SortGPA.items(), key=lambda x: x[1], reverse=True)
                    stdscr.addstr("\nGPA Rankings:\n")
                    for rank, (student_id, gpa) in enumerate(sorted_gpa, 1):
                        stdscr.addstr(f"Rank {rank}: Student ID {student_id} - GPA: {gpa}\n")
                    stdscr.addstr("\nPress any key to continue...")
                    stdscr.refresh()
                    stdscr.getch()
            
            elif choice == "6":  # Display all data
                stdscr.addstr("\nStudents:\n")
                for student in StudentList:
                    stdscr.addstr(str(student) + "\n")
                stdscr.addstr("\nCourses:\n")
                for course in CourseList:
                    stdscr.addstr(str(course) + "\n")
                stdscr.addstr("\nMarks:\n")
                for mark in MarkList:
                    stdscr.addstr(str(mark) + "\n")
                stdscr.addstr("\nPress any key to continue...")
                stdscr.refresh()
                stdscr.getch()
            
            elif choice == "7":  # Exit
                display_message(stdscr, "Goodbye!")
                break
            
            else:  # Invalid choice
                display_message(stdscr, "Invalid choice! Try again.")
        
        except ValueError:
            display_message(stdscr, "Invalid input. Please try again.")

# Run the program
wrapper(management)