# learnpy 

[| Python Basic](https://github.com/tristaaa/learnpy/blob/master/README.md#-python-basic)<br>
&ensp;&ensp;[Introduction to Python](https://github.com/tristaaa/learnpy/blob/master/README.md#-introduction-to-python)<br>
&ensp;&ensp;[Core Elements of Programs](https://github.com/tristaaa/learnpy/blob/master/README.md#-core-elements-of-programs)<br>
[| Simple Program](https://github.com/tristaaa/learnpy/blob/master/README.md#--simple-program)<br>
&ensp;&ensp;[Simple Algorithms](https://github.com/tristaaa/learnpy/blob/master/README.md#-simple-algorithms)<br>
&ensp;&ensp;[Functions](https://github.com/tristaaa/learnpy/blob/master/README.md#-functions)<br>
&ensp;&ensp;[Complete Program](https://github.com/tristaaa/learnpy/blob/master/README.md#-complete-program)<br>


## | Python Basic
### 1.1 Introduction to Python

### 1.2 Core Elements of Programs

## | Simple Program
### 2.1 Simple Algorithms
1) bisectionSearch_1.py

    get the guess square root of x which is greater than 1
2) bisectionSearch_2.py

    get the guess square root of x which is a positive fraction
3) bisectionSearch_3.py (small test)

    this create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Thus, 
- the Bisection Search converges on the order of $\log_2 N$ steps
- Bisection Search works when value of function varies monotonically with input


1) decimalFractionToBinary.py

    turn a decimal fraction to its binary form. But if the frctions are not ones where the denominator is a whole power of 2, then the fraction cannot be represent exactly.   So we should use `abs(x-y) < epsilon` rather than `x==y` when compare two floats.

1) newtonRaphson.py

    Newton-Raphson Method to get an approximate root of number. It says that if g is an approxiamte root of x, then `g - p(g)/p'(g)` is a better answer.

### 2.2 Functions
So far, we've 

- covered language mechanism, the first notion of `while` and `for` loops, and therefore, of iterations.
- know how to write different files for each computation
- each file is some piece of code that saves away on the machine
- each code is a sequence of instructions
    
But, there're problems with this approach

- easy for small-scale problems
- messy for larger issues
- hard to keep track of details
    
**Function**: mechanism to achieve *decomposition* (sometimes called modularity) and *abstraction*

Analogy ：  a PROJECTOR
 >- it's a black box
 >- don't know how it works
 >- know the interface: input & output
 >- connect any electronics to it that can communicate with that input
 >- black box somehow converts image from input source to a wall or screen, magnifying it
 >- *ABSTRACTION*：do not need to know how projector works to use it 

Then if we want to produce a large image, we need more than one projectors
>- all projectors work together to produce larger image
>- *DECOMPOSITION* ：different devices work together to achieve an end goal

==>
>*DECOMPOSITION* ： divide code into **modules**
 >- **self-contained**
 >- used to **break up** code
 >- intended to be **reusable**
 >- keep code **organized**
 >- keep code **coherent**
>*ABSTRACTION* ：suppress details of method to compute something from use off that computation
 >- think of a piece of code as a **black box**
 >- cannot see details
 >- do not need or want to see details
 >- hide tedious coding details
 
 **function** has a name, parameters(0 or more), a docstring(optional), a body
 ![](http://img.blog.csdn.net/20180111165535757?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdHNvb3R3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 ITERATIVE or RECURSIVE
 1) gcd.py
 
     use two ways(iterative / recursive) to find the greatest common divisor
 2) hanoi.py

    Tower of hanoi consists of three rods and some disks of different sizes, the object of the puzzle is to move the entire stack of disks to another rod, following some rules:<br>
    >- Only one disk can be moved at a time
    >- Each move consists of taking the upper disk from one stacks and placing it on the top of another stack
    >- No disk may be placed on top of a smaller disk  
    Let's named the three rod of A, B and C, now we need to move n disks from A to C, and the program goes like:

    ```python
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
            hanoi(n - 1, a, b, c)  # move the n-1 tower from `a` to `b` in assist of `c`
            moveDisk(n, a, c)  # move No.n disk from `a` to `c`
            hanoi(n - 1, b, c, a)  # move the n-1 tower from `a` to `b` in assist of `c`

    hanoi(3, 'A', 'C', 'B')  # move 3 disk from A to C
    ```

 3) fibonacci.py

    calculate the total number of female rabbits after n month(s), take the prerequisites
    that at the beginning there are one male and one female rabbit in a pen that are immature to be pregnant, and it takes one month for them to give birth to two rabbits(male and female), and all the rabbits never die.

    So, when n=0(beginning), female=1; when n=1, female=1(pregnant); when n=2, female=2(one pregnant and another not)...

    The program goes like the following:

    ```python
    def fib(n):
        '''
        input: n represent the month
        return: the number of the total female after n mmonth(s)
        '''
        if n==0 or n==1:
            return 1
        else:
            # the number equals to the number one month earlier:fib(n-1)
            # plus the newborn rabbit that are the children of the fib(n-2) rabbits
            return fib(n-1)+fib(n-2)  
    ```

### 2.3 Complete Program
