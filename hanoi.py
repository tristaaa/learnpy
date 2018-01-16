#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def moveDisk(n, a, c):
    print('Move No.', n, 'disk from', str(a), 'to', str(c))

def hanoi(n, a, c, b):
    '''
    input: move n disks from `a` to `c` in assist of `b`
    No. 1 disk is the smallest disk
    try to show the order of all the movement
    return: none
    '''
    if n == 1:
        moveDisk(1, a, c)
    else:
        # move the n-1 tower from `a` to `b` in assist of `c`
        hanoi(n - 1, a, b, c)
        moveDisk(n, a, c)  # move No.n disk from `a` to `c`
        # move the n-1 tower from `a` to `b` in assist of `c`
        hanoi(n - 1, b, c, a)


hanoi(3, 'A', 'C', 'B')
