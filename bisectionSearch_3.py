#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# use bisection search to guess the secret number
# the user thinks of an integer [0,100).
# The computer makes guesses, and you give it input 
# - is its guess too high or too low? 
# Using bisection search, the computer will guess the user's secret number

low = 0
high = 100
guess = (low+high)//2
print('Please think of a number between 0 and 100!')
while True:
    print('Is your secret number '+str(guess)+'?')
    is_secret_num = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if is_secret_num =='l':
        low = guess
    elif is_secret_num =='h':
        high = guess
    elif is_secret_num =='c':
        break
    else:
        print('Sorry, I did not understand your input.')
    guess = (low+high)//2
print('Game over. Your secret number was:',guess)