#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# use Bisection Search to get a close enough guess to the root of x
# Suppose x=26
# Bisection Search makes it quicker to find the approximate square root of x 
# which uses just 13 times to get the close enough square root of x
 
x = 26
epsilon = 0.01
low=1
high=x
guess=(low+high)/2
num=0
while abs(guess**2-x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high=guess
    guess=(low+high)/2
    num+=1
if abs(guess**2-x)>=epsilon:
    print('Failed on x root of',x)
else:
    print('num_guesses =',num)
    print(guess, 'is close to the x root of', x)
