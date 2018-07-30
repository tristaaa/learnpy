#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 
import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        """return self's last name"""
        return self.lastName
    def __str__(self):
        """return self's name"""
        return self.name
    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        """return self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        """return True if self's name is lexicographically less than other's name,
        and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName


#example usage

p1 = Person('Mark Zuckerburg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e) 
# shows Mark Zuckerburg, Drew Houston, Bill Gates, Andrew Gates, Steve Wozniak in each line

personList.sort()
print()

for e in personList:
    print(e)
# shows Andrew Gates, Bill Gates, Drew Houston, Steve Wozniak, Mark Zuckerburg in each line