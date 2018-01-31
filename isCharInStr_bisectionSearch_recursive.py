#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0 or len(aStr) == 1:
        return char == aStr
    elif char == aStr[len(aStr) // 2]:
        return True
    elif char < aStr[len(aStr) // 2]:
        return isIn(char, aStr[:len(aStr) // 2])
    else:
        return isIn(char, aStr[len(aStr) // 2 + 1:])


print(isIn('c', ''))
print(isIn('c', 'b'))
print(isIn('c', 'abdfde'))
print(isIn('c', 'abcgr'))
print(isIn('g', 'abcdghr'))
