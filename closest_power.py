# -*- coding: utf-8 -*-

dedef closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0
    epsilon = num-base**exponent
    while base**exponent < num:
        exponent +=1
        if base**exponent > num:
            exponent -= 1
            break
        if epsilon > num-base**exponent:
            epsilon = num-base**exponent
    if epsilon > base**(exponent+1)-num:
        epsilon = base**(exponent+1)-num
        return exponent+1
    else:
        return exponent
        

closest_power(3,1) #0
closest_power(3,3) #1
closest_power(3,4) #1
closest_power(3,8) #2
closest_power(3,12) #2
closest_power(3,25) #3