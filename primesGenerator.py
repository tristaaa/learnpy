#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 

def genPrimes(x = 1):
    primesList = [2]
    yield 2
    while True:
#       x += 1
        x += 2 # more efficient
        for p in primesList:
            if x % p == 0:
                break
        else: 
        # executed only when the primeList is exhausted, but when the loop break,
        # it won't executed
            primesList.append(x)
            yield x

def genPrimes2(x = 1):
    """Another good code sample"""
    primesList = [2]
    yield 2
    while True:
        x += 2
        if all(x%p != 0 for p in primesList):
            """all(iterable) method only returns True if 
            each element of the para iterable is True(False when 
            the element is Flase, or 0, or empty)
            Notice: all([]) or all(()) returns True"""
            yield x
            primesList.append(x)


def genPrimesFn1():
    '''Function to return 1000000 prime numbers'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    while len(primes) < 1000000:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
    return primes

def genPrimesFn2():
    '''Function to print every 10th prime 
    number, until you've printed 20 of them.'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    counter = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            counter += 1
            if counter % 10 == 0:
                # Print every 10th prime
                print(last)
            if counter % (20*10) == 0:
                # Quit when we've printed the 10th prime 20 times (ie we've
                # printed the 200th prime)
                return



def genPrimesFn3():
    '''Function to keep printing the prime number until the user stops the program.
    This way uses user input; 
    you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    uinp = 'y'    # Assume we want to at least print the first prime...
    while uinp != 'n':
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            print(last)
            uinp = input("Print the next prime? [y/n] ")
            while uinp != 'y' and uinp != 'n':
                print("Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no.")
                uinp = input("Print the next prime? [y/n] ")



# pri = genPrimes()
pri = genPrimes2()
print(pri.__next__()) # show 2
print(pri.__next__()) # show 3
print(pri.__next__()) # show 5
print(pri.__next__()) # show 7
print(pri.__next__()) # show 11
print(pri.__next__()) # show 13
print(pri.__next__()) # show 17
print(pri.__next__()) # show 19
print(pri.__next__()) # show 23
print(pri.__next__()) # show 29