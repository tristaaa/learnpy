#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 
from personTrial import Person

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum # MITPerson attribute:unique ID
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        # sorting MIT people uses their ID number, not name!
        return self.idNum < other.idNum
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)


# MITPerson usage example

m3 = MITPerson('Mark Zuckerburg')
Person.setBirthday(m3,5,14,84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,3,4,83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,10,28,55)

MITPersonList = [m1,m2,m3]

print('')
print('---MITPerson usage example---')

for e in MITPersonList:
    print(e)
# shows Bill Gates, Drew Houston, Mark Zuckerburg in each line

MITPersonList.sort()
print()

for e in MITPersonList: 
    print(e)
# shows Mark Zuckerburg, Drew Houston, Bill Gates in each line(sorting by ID)

mp1 = MITPerson('Eric')
mp2 = MITPerson('John')
mp3 = MITPerson('John')
mp4 = Person('John')

print()
print(mp1 < mp2) # shows True
print(mp4 < mp1) # shows Flase
# print(mp1 < mp4) # shows AttributeError: 'Person' object has no attribute 'idNum'