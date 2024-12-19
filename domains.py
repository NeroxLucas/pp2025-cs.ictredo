import numpy as np  # type: ignore

StudentList = []
CourseList = []
MarkList = []  
SortGPA = {}  

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
