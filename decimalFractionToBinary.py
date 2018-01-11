#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# There is simple way to get the binary form of a fraction
#
# First, if the number x is a decimal integer,
# then the remainder relative to 2(x%2) of the number is the last binary bit
# and if devide x by 2(x//2), all the binary bits get shifted right
#   eg. 19=10011 ---> 19//2=9=1001  i.e. 1001 is the first 4 bit of 10011
# So, we can get its binary using the following program:
#
#   num = int(input('Enter a integer: '))
#   if num <0:
#       isNeg=True
#       num = abs(num)
#   else:
#       isNeg = False
#   result = ''
#   while num>0:
#       result = str(num%2) + result
#       num //= 2
#   if isNeg:
#       result = '-' + result
#   print(result)
# Then, as to a decimal fraction, like 5/8=0.675
# we can fisrt multipule by a power of 2 big enough to convert it to a integer
# like, 5/8*(2**3)=5 next, do the same way as before, we get the binary(101)
# finnally, divide by the (2**3), means shift right 3 points ==> (0.101)
# this also work for fractions that are bigger than 1
#
#   SOME IMPLICATIONS
#   - If there isn't an integer p that x*(2**p) is a whole number, then internal
#     representation of x is always an approximation
#     若 x 乘 2**p 无法成为一个整数，则在计算机内部它存储的只是一个近似值
#   - Tesing equality of floats is not exact: so use abs(x-y)< epsilon rather x==y
#   - So, why does ```print(0.1)``` return 0.1, if not exact?
#     Because python designers set it up this way to automatically round


x = float(input('Enter a positive fraction :'))
p = 0
while ((2**p) * x) % 1 != 0:
    print('Reaminder = ' + str((2**p) * x - int((2**p) * x)))
    p += 1
num = int(x * (2**p))
result = ''
while num > 0:
    result = str(num % 2) + result
    num //= 2
for i in range(p - len(result) + 1):
    result = '0' + result
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of decimal ', str(x), 'is', str(result))
