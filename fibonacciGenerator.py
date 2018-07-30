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

print(fib.__next__()) # shows 1
print(fib.__next__()) # shows 2
print(fib.__next__()) # shows 3
print(fib.__next__()) # shows 5
print(fib.__next__()) # shows 8
