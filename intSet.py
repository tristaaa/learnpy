#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

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
        # ... the following four lines are functionally equivalent to the next one line
        # result = ''
        # for e in self.vals:
        #     result = result + str(e) + ","
        # return "{" + result[:-1] + "}"
        return "{" + ",".join([str(e) for e in self.vals]) + "}"

    def intersect(self, other):
        s3 = intSet()
        for e1 in self.vals:
            if e1 in other.vals:
                s3.insert(e1)
        return s3

    def __len__(self):
        return len(self.vals)

s = intSet()
print(s) # it shows {}
s.insert(2)
s.insert(3)
s.insert(2)
print(s) # it shows {2,3}
s.member(3) # it shows True
s.remove(2)
print(s) # it shows {3}

# it raises an self-defined error -> ValueError: 3 not found   
# following by the system defined error -> ValuError: list.remove(x): x not in list
# s.remove(2) 

s2 = intSet()
s2.insert(5)
s2.insert(6)
s2.insert(3)
print(s.intersect(s2))

print(len(s2))