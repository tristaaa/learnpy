#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def  __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        newNumer = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        newDenom = self.getDenom() * other.getDenom()
        return fraction(newNumer, newDenom)
    def __sub__(self, other):
        newNumer = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        newDenom = other.getDenom() * self.getDenom()
        return fraction(newNumer, newDenom)
    def convert(self):
        return self.getNumer() / self.getDenom()


onHalf = fraction(1,2)
twoThirds = fraction(2,3)
newFraction = onHalf + twoThirds
newFraction2 = onHalf - twoThirds
print(newFraction) # it shows 7/6
print(newFraction2) # it shows -1/6