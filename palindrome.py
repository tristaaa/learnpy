#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def isPalindrome(s):
    '''
    test and show whether the input string is or not a palindrome
    '''

    def toChars(s):
        s = s.lower()
        ans = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvw':
                ans += char
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


str1 = 'Able was I, ere I saw ELBA'
str2 = 'haha'
print('string:', str1, 'is ' + ['not ', ''][isPalindrome(str1)] + 'a palindrome')
print('string:', str2, 'is ' + ['not ', ''][isPalindrome(str2)] + 'a palindrome')
