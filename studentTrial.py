#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 
from MITPersonTrial import MITPerson

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)


# Student usage example

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')

studentList = [s1,s2,s3,s4]

print('')
print('---Student usage example---')
print(s1) # shows Matt Damon
print(s1.getClass()) # shows 2017
print(s1.speak('where is the quiz?')) # shows Damon says: Dude, where is the quiz?
print(s2.speak('i have no idea')) # shows Affleck says: Dude, i have no idea