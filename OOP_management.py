StudentList = [];
CourseList = []

class Student:
    def __init__(self,StudentName, StudentID):
        self.StudentName = StudentName
        self.StudentID = StudentID
    def __str__(self):
        return f"Student: {self.StudentName} - ID: {self.StudentID}"
    

class Course:
    def __init__(self,CourseName, CourseID):
        self.CourseName = CourseName
        self.CourseID = CourseID
    def __str__(self):
        return f"Course: {self.CourseName} -  ID: {self.CourseID}"
    

class Mark:
    def __init__(self, StudentID, CourseID, mark):
        self.StudentID = StudentID
        self.CourseID = CourseID
        self.mark = mark
    def __str__(self):
        return f"Student ID: {self.StudentID} - Grade in Course ID {self.CourseID}: {self.mark}"


def management():
    MarkList = [] #List to store marks
    while True:
        print("\nEnter your choice:")
        print("1.Add students")
        print("2.Add course")
        print("3.Add student mark")
        print("4.Display")
        print("5.Exit")

        try:
            user_input = int(input("Enter your choice "))
            if user_input == 1:
                stdname = input("Enter student name: ")
                stdid = int(input("Enter student ID: "))
                #use for run for loops
                student = Student(stdname, stdid)
                StudentList.append(student)
                print("Successfully added!")

            elif user_input == 2:
                crsname = input("Enter course name: ")
                crsid = int(input("Enter course ID:"))
                #use for run for loops
                course = Course(crsname, crsid)
                CourseList.append(course)
                print("Successfully added!")

            elif user_input == 3:
                stdid = int(input("Enter existing student ID: "))
                crsid = int(input("Enter existing course ID: "))
                mark = int(input("Enter the mark: "))

                #Check if student and course exist
                student_exists = any(student.StudentID == stdid for student in StudentList)
                course_exists = any(course.CourseID == crsid for course in CourseList)

                if not student_exists:
                    print("Not exists")
                elif not course_exists:
                    print("Not exist")
                else:
                    new_mark = Mark(stdid, crsid, mark)
                    MarkList.append(new_mark)
                    print(f"Mark is successfully added")

            elif user_input == 4:
                print("\nStudents:")
                for student in StudentList:
                    print(student)

                print("\nCourses:")
                for course in CourseList:
                    print(course)

                print("\nMarks:")
                for mark in MarkList:
                    print(mark)
            
            elif user_input == 5:
                print("Goodbye")
                break

            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")


#run the programm
management()
