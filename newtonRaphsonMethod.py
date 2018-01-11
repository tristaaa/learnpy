#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# There is another way to get an approximate root of x using Newton-Raphson Method
# If we want to find roots of a polynomial in one variable:
#   p(x) = An * x^n + An-1 * x^(n-1) + ... + A1 * x + A0
# So, if we find r that make the p(r)=0, we get the approximate root
# eg. find the square root of 24, find the root of p(x) = x^2 - 24
#
# Newton showed that if g is an approximation to the root, then
#   g - p(g)/p'(g)  is a better solution, where p' is derivative of p

num = 54.0
epsilon = 0.01
guess = num / 2.0
num_guess = 0
while abs(guess**2 - num) >= epsilon:
    guess = guess - ((guess**2) - num) / (2 * guess)
    num_guess += 1
print('num_guesses = ', num_guess)
print('qure root of ' + str(num) + ' is about ' + str(guess))
