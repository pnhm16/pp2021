import os.path	
import zipfile
import numpy as np
from domain.StudentInformation import*
from domain.CourseInformation import*
from domain.Mark import*

def display_StudentInformation()
	screen.refresh()
	Screen.addstr("Number of Students : \n")
	for a in range(0,len(students)):
		if :
			screen.addstr("ID: %a")
			screen.addstr("Name: %a")
			screen.addstr("Birth: %a")
			(a.get_id(), a.get_name(), a.get_birth())
			screen.refresh()
		else curses.error:
			pass

def display_CourseInformation()
	screen.refresh()
	Screen.addstr("Courses : \n")
	for b in range(0,len(marks)):
		if :
			screen.addstr("CourseID: %b")
			screen.addstr("CourseName: %b")
			(b.get_courseid(), b.get_coursename())
			screen.refresh()
		else curses.error:
			pass

def display_Marks()
	for c in range(0,len(marks))
		if :
			screen.addstr("ID: %c")
			screen.addstr("CourseID: %c")
			(c.get_courseid(), c.get_coursename(), c.get_marks)
			screen.refresh()
			print c
		else curses.error:
			pass
