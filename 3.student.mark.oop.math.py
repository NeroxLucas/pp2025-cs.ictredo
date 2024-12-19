import math
import numpy as np
import curses
from curses import wrapper 

StudentList = []
CourseList = []

class Student:
    def __init__(self, StudentName, StudentID):
        self.StudentName = StudentName
        self.StudentID = StudentID
    def __str__(self):
        return f"Student: {self.StudentName} - ID: {self.StudentID}"


class Course:
    def __init__(self, CourseName, CourseID):
        self.CourseName = CourseName
        self.CourseID = CourseID
    def __str__(self):
        return f"Course: {self.CourseName} - ID: {self.CourseID}"


class Mark:
    def __init__(self, StudentID, CourseID, mark):
        self.StudentID = StudentID
        self.CourseID = CourseID
        self.mark = mark
    def __str__(self):
        return f"Student ID: {self.StudentID} - Grade in Course ID {self.CourseID}: {self.mark}"


def calculate_gpa(student_id, MarkList):
    student_marks = [mark.mark for mark in MarkList if mark.StudentID == student_id]
    if student_marks:   #check if the student_marks is empty
        gpa = np.mean(student_marks)
        return round(gpa, 2)
    return None


def management(stdscr):
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
    MarkList = []  # List to store marks
    SortGPA = {}  # Dictionary to rank GPA

    while True:
        stdscr.clear()  # Clear the screen
        stdscr.addstr("Enter your choice:\n", curses.A_BLINK)
        stdscr.addstr("1. Add students\n", curses.color_pair(1))
        stdscr.addstr("2. Add course\n", curses.color_pair(1))
        stdscr.addstr("3. Add student mark\n", curses.color_pair(1))
        stdscr.addstr("4. Display GPA\n", curses.color_pair(1))
        stdscr.addstr("5. Ranking GPA\n", curses.color_pair(1))
        stdscr.addstr("6. Display\n", curses.color_pair(1))
        stdscr.addstr("7. Exit\n", curses.color_pair(1))
        stdscr.addstr("Your choice: ", curses.color_pair(1))

        stdscr.refresh()  # Refresh the screen

        try:
            # Capture user input as bytes and decode to string
            user_input = stdscr.getstr().decode("utf-8").strip()

            if user_input == "1":
                stdscr.addstr("\nEnter student name: ")
                stdscr.refresh()
                stdname = stdscr.getstr().decode("utf-8").strip()

                stdscr.addstr("\nEnter student ID: ")
                stdscr.refresh()
                stdid = int(stdscr.getstr().decode("utf-8").strip())

                student = Student(stdname, stdid)
                StudentList.append(student)
                stdscr.addstr("\nSuccessfully added!\n")

            elif user_input == "2":
                stdscr.addstr("\nEnter course name: ")
                stdscr.refresh()
                crsname = stdscr.getstr().decode("utf-8").strip()

                stdscr.addstr("\nEnter course ID: ")
                stdscr.refresh()
                crsid = int(stdscr.getstr().decode("utf-8").strip())

                course = Course(crsname, crsid)
                CourseList.append(course)
                stdscr.addstr("\nSuccessfully added!\n")

            elif user_input == "7":
                stdscr.addstr("\nGoodbye!\n")
                stdscr.refresh()
                break

            else:
                stdscr.addstr("\nInvalid choice. Try again.\n")

            stdscr.addstr("\nPress any key to continue...")
            stdscr.refresh()
            stdscr.getch()  # Wait for key press to continue

        except ValueError:
            stdscr.addstr("\nInvalid input. Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()  # Wait for key press to continue

# Run the program
wrapper(management)
"""The key=lambda x: x[1] specifies that the sorting should be based on the second element (GPA) of each tuple.
reverse=True ensures the sorting is done in descending order"""