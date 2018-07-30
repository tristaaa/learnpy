#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 
from studentTrial import UG, Grad

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = [] # list of Student objects
        self.grades = {} # maps isNum -> list of grades
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
            Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades fprstudent"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book') 

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:
            #Important!!!  return a copy of grade, using [:]
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
#       return self.students[:] # return copy of list of student
        for s in self.students:
            yield s

def gradeReport(course):
    """Assumes: course is of type Grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + 'has no grades')
    return '\n'.join(report)


# usage example
# four undergraduate students and two graduate students
print()
print('---Grade Report for Students---')


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)


six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print()
print(gradeReport(six00))

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)

print()
print(gradeReport(six00))