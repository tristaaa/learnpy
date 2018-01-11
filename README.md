#learnpy 
---
1. bisectionSearch_1.py

    get the guess square root of x which is greater than 1
2. bisectionSearch_2.py

    get the guess square root of x which is a positive fraction
3. bisectionSearch_3.py (small test)

    this create a program that guesses a secret number!
    >The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
```
Thus, 
* the Bisection Search converges on the order of $\log_2 N$ steps
* Bisection Search works when value of function varies monotonically with input

1. decimalFractionToBinary.py

    turn a decimal fraction to its binary form. 
    >But if the frctions are not ones where the denominator is a whole power of 2, then the fraction cannot be represent exactly.   So we should use `abs(x-y) < epsilon` rather than `x==y` when compare two floats.