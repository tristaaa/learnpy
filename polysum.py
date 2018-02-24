#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from math import *


def polysum(n, s):
    '''
    input: n numbers of sides, each side has length s
    return: the sum of the area and the square of the perimeter of the regular polygon
    '''
    p_area = (0.25 * n * (s ** 2)) / tan(pi / n)
    p_per = n * s
    return round((p_area + p_per**2), 4)
