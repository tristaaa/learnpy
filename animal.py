#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""): 
        self.name = newname
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)

class Cat(Animal):
    def speak(self): # new method
        print("meow")
    def __str__(self): # override
        return "cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        # zfill(num) is a method on a string to pad the beginning with zores
        return str(self.rid).zfill(3) # eg. return 001 instead of 1
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class, means the child of self and other
        return Rabbit(0, self, other)
    def __eq__(self, other):
        # decide two rabbits are equal if they have the same two parents
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parent_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid ==other.parent2.rid
        return parent_same or parent_opposite

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age) # call Animal constructor
        Animal.set_name(self, name) # call Animal's method
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", diff, "years younger than", other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
    
import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random() # gives back float between [0,1)
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r <0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)


jelly = Cat(2)
jelly.set_name("jelly")
print(jelly) # shows cat:jelly:2
jelly.speak() # shows meow

eric = Person("Eric", 50)
john = Student("John", 19, "CS")
print(john) # shows John:19:CS
john.change_major("DTIN")
print(john) # shows John:19:DTIN

eric.age_diff(john) # shows Eric is 31 years older than John