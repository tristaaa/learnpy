#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# The greatest common divisor of two positive integers is
# the largest integer that divides each of them without remainder.
# there're two(or more than two) ways to calculate the gcd(a,b)
# One, begin with a test value equals to the smaller of the two input arguments,
#   and iteratively reduce this value by 1 until either reach a case where
#   the value divide both a and b without a remainder, or reach 1
#
# The other, as Euclid's algorithm says, gcd(a,b)=gcd(b,r0=a%b)=gcd(r0,r1=b%r0)=...=gcd(rN-2,rN-1)=gcd(rN-1,0)=rN-1
#   and finally, when the remainder rN=0, its next predecessor rN-1 is the greatest common divisor
#   the k-th step is to find a quotient qk and remainder rk that satisfy the equation:
#       rk-2 = qk * rk-1 + rk


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.

    strat with the smaller value of a, b
    then iteratively reduce it by 1
    stop when either find a number that can divide both a and b, or it is 1
    '''
    result = a > b and b or a  # result is the smaller one of a,b; same as: result =[a,b][a>b]
    while (a % result != 0 or b % result != 0) and result > 1:
        result -= 1
    return result


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.

    Euclidean's Algorithm:

    if b==0, return a
    else gcd(a, b)=gcd(b, a%b)
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


print('(use Iterative notion) The greatest common divisor of 12 and 9 :', gcdIter(12, 9))
print('(use Recursive notion) The greatest common divisor of 12 and 9 :', gcdRecur(12, 9))
