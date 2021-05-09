import math
import numpy as np
import curses

Students = []
StudentID = []
Course = []
Marks = []

class Student
def get_Number_of_pupils()
    number_of_pupils = a
    a = int(input("Enter class's pupils number: "))
    return a

def get_Student_information(number_of_pupils)
    self.Student_ID = input(a1)
    self.Student_name = input(a2)
    self.Student_DOB = input(a3)
    a1 = "Enter ID: "
    a2 = "Enter Name: "
    a3 = int("Enter birth: ")
        for a3 in range(1000,2021)
            print("Invalid")
        else
            return a3
    return a1, a2, a3

def display_Student_information()
    print("Class's Student:\n" + student[i].get("a"))
    for i in range(0,len(marks))
        print("Student ID: " + students[i].get("a1"), "Student name: " + student[i].get("a2"), "Student DOB: " + student[i].get("a3"))
    screen.refresh()

class Course

def get_Number_of_courses
    Number_of_courses = b
    a4 = int(input("Enter Number of Courses"))
    return b

def get_Course_information
    Course_ID = input(b1)
    Course_name = input (b2)
    b1 = "Enter Course ID "
    b2 = "Enter Course Name "
    return b1, b2

def display_Course_information()
    print("Number of courses : \n" + course[i].get("b"))
    for i in range(0,len(course))
        print("Course ID: " + course[i].get("b1"), "Course name: " + course[i].get("b2"))
    screen.refresh()

class Marks

def get_Marks
    for i in range(0, len(student))
        marks.append({course: })
        mark = c
        c = float(input("Enter Mark: "))
        marks[i].update({course: mark})

def display_marks()
    for i in range(0, len(student))
        print("Student marks: " + course[i].get("c"))
    screen.refresh()

class GPA
    
    def get_GPA(self, courses)
        sum_credits = 0
        for i in range(0, len(courses))
            sum_credits = int(self.marks[i][2])
            self.gpa = int(self.marks[i][1] * self.marks[i][2])

        self.GPA = math.floor((self.GPA / sum_credits) * 20) / 20
    self_course = input("Select course: ")
    display_marks()
    screen.refresh()


        return self_GPA    
