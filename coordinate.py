#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class Coordinate(object):
    def __init__(self, x, y):
        """
        self : parameter to refer to an instance of the class
        x, y(in line 2) : what data initializes a **Coordinate** object
        self.x, self.y : two data attributes for every **Coordinate** object
        """
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __sub__(self,other):
        return (self.x-other.x, self.y-other.y)

    def __eq__(self,other):
        # First make sure `other` is of the same type 
        assert type(other) == type(self)
        # Since `other` is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return "Coordinate("+ str(self.getX()) +","+ str(self.getY()) +")"

c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x) # will show 3

dist1 = c.distance(origin)
print(dist1) # will show 5.0
dist2 = Coordinate.distance(c,origin)
print(dist2) # will also show 5.0

print(c) # will show <3,4>

print(c.getX())

c1 = Coordinate(3,4)
c2 = Coordinate(4,4)
print(c==c1)
print(c==c2)

print(repr(c)) # shows Coordinate(3,4)
print(eval(repr(c))) # shows <3,4>
print(eval(repr(c)) == c) # return True

