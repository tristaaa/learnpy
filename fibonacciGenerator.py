#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 

def genFib():
    fibn_1 = 1 # fib(n-1)
    fibn_2 = 0 # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

fib = genFib()
print(fib) # shows <generator object genTest at 0x11bfd3620>
print(fib.__iter__())  # shows <generator object genTest at 0x11bfd3620>

print(fib.__next__()) # shows 1
print(fib.__next__()) # shows 2
print(fib.__next__()) # shows 3
print(fib.__next__()) # shows 5
print(fib.__next__()) # shows 8


#
#-----------------------------------
def fibonacci(n):
    """Have to calculate all the former fibonacci number by the order""" 
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)


def _fib(n, fibs = [(0, 1), (1, 1)]):
    """Returns the tuple (Fib(n), Fib(n+1))"""
    try:
        f = fibs[n]
    except IndexError:
        a, b = _fib(n // 2) # Fib(n-2), Fib(n-1)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            fibs.append((c, d))
        else:
            fibs.append((d, c + d))
            print('in fibs:',fibs)
        f = fibs[-1]
    return f


print(fibonacci(2)) 
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
