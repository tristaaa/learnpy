#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Now, if x is a fraction rather than numbers bigger than 1
# then things change a little
# the final guess lies between x and 1 rather than 1 to x or 0 to x
# Suppose x = 0.6

x = 0.6
epsilon = 0.01
low = x
high = 1
guess = (low+high)/2
num_guesses = 0
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (low+high)/2
    num_guesses +=1
if abs(guess**2 - x) >=epsilon:
    print('Fail on square root of', x)
print('num_guesses =',num_guesses)
print(guess, 'is close to square root of', x)