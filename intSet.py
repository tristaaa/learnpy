#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 

class intSet(object):
    def __init__(self):
        self.vals = [] # start with an empty list
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + " not found")
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ","
        return "{" + result[:-1] + "}"

s = intSet()
print(s) # it shows {}
s.insert(2)
s.insert(3)
s.insert(2)
print(s) # it shows {2,3}
s.member(3) # it shows True
s.remove(2)
print(s) # it shows {3}
s.remove(2) # it shows ValueError: 3 not found