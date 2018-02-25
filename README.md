# learnpy 

[| Python Basic](https://github.com/tristaaa/learnpy/blob/master/README.md#-python-basic)<br>
&ensp;&ensp;[Introduction to Python](https://github.com/tristaaa/learnpy/blob/master/README.md#11-introduction-to-python)<br>
&ensp;&ensp;[Core Elements of Programs](https://github.com/tristaaa/learnpy/blob/master/README.md#12-core-elements-of-programs)<br>
[| Simple Program](https://github.com/tristaaa/learnpy/blob/master/README.md#-simple-program)<br>
&ensp;&ensp;[Simple Algorithms](https://github.com/tristaaa/learnpy/blob/master/README.md#21-simple-algorithms)<br>
&ensp;&ensp;&ensp;&ensp;[Bisection Search](https://github.com/tristaaa/learnpy/blob/master/README.md#bisection-search)<br>
&ensp;&ensp;[Functions](https://github.com/tristaaa/learnpy/blob/master/README.md#22-functions)<br>
&ensp;&ensp;&ensp;&ensp;[Iterative or Recursive](https://github.com/tristaaa/learnpy/blob/master/README.md#iterative-or-recursive)<br>
&ensp;&ensp;&ensp;&ensp;[Divide and Conquer](https://github.com/tristaaa/learnpy/blob/master/README.md#divide-and-conquer)<br>
&ensp;&ensp;[Complete Programming Experience:polysum](https://github.com/tristaaa/learnpy/blob/master/README.md#23-complete-programming-experiencepolysum)<br>
[| Structured Types](https://github.com/tristaaa/learnpy/blob/master/README.md#-structured-types)<br>
&ensp;&ensp;[Tuples and Lists](https://github.com/tristaaa/learnpy/blob/master/README.md#31-tuples-and-lists)<br>
&ensp;&ensp;[Dictionaries and Sets](https://github.com/tristaaa/learnpy/blob/master/README.md#32-dictionaries-and-sets)<br>
[| Midterm Exam](https://github.com/tristaaa/learnpy/blob/master/README.md#-midterm-exam)<br>
[| Good Programming](https://github.com/tristaaa/learnpy/blob/master/README.md#-good-programming)<br>
&ensp;&ensp;[Testing and Debugging](https://github.com/tristaaa/learnpy/blob/master/README.md#41-testing-and-debugging)<br>
&ensp;&ensp;[Exceptions and Assertions](https://github.com/tristaaa/learnpy/blob/master/README.md#42-exceptions-and-assertions)<br>
[| Object Oriented Programming](https://github.com/tristaaa/learnpy/blob/master/README.md#-object-oriented-programming)<br>
&ensp;&ensp;[Classes and Inheritance](https://github.com/tristaaa/learnpy/blob/master/README.md#51-classes-and-inheritance)<br>
&ensp;&ensp;[An Extended Example](https://github.com/tristaaa/learnpy/blob/master/README.md#52-an-extended-example)<br>
[| Algorithmic Complexity](https://github.com/tristaaa/learnpy/blob/master/README.md#-algorithmic-complexity)<br>
&ensp;&ensp;[Computational Complexity](https://github.com/tristaaa/learnpy/blob/master/README.md#61-computational-complexity)<br>
&ensp;&ensp;[Searching and Sorting Algorithms](https://github.com/tristaaa/learnpy/blob/master/README.md#62-searching-and-sorting-algorithms)<br>
[| Plotting](https://github.com/tristaaa/learnpy/blob/master/README.md#-plotting)<br>
&ensp;&ensp;[Plotting](https://github.com/tristaaa/learnpy/blob/master/README.md#71-poltting)<br>


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

#### BISECTION SEARCH
the Bisection Search converges on the order of <img src="https://latex.codecogs.com/gif.latex?\inline&space;log_2&space;N" title="log_2 N" /></a> steps
Bisection Search works when value of function varies monotonically with input


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
- it's a black box
- don't know how it works
- know the interface: input & output
- connect any electronics to it that can communicate with that input
- black box somehow converts image from input source to a wall or screen, magnifying it
- *ABSTRACTION*：do not need to know how projector works to use it 

Then if we want to produce a large image, we need more than one projectors
- all projectors work together to produce larger image
- *DECOMPOSITION* ：different devices work together to achieve an end goal

==>
*DECOMPOSITION* ： divide code into **modules**
- **self-contained** 
- used to **break up** code
- intended to be **reusable**
- keep code **organized**
- keep code **coherent**
*ABSTRACTION* ：suppress details of method to compute something from use off that computation
- think of a piece of code as a **black box**
- cannot see details
- do not need or want to see details
- hide tedious coding details
 
 **function** has a name, parameters(0 or more), a docstring(optional), a body
 ![](http://img.blog.csdn.net/20180111165535757?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdHNvb3R3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 #### ITERATIVE or RECURSIVE
 1) gcd.py
 
     use two ways(iterative / recursive) to find the greatest common divisor
 2) hanoi.py

    Tower of hanoi consists of three rods and some disks of different sizes, the object of the puzzle is to move the entire stack of disks to another rod, following some rules:<br>
    - Only one disk can be moved at a time
    - Each move consists of taking the upper disk from one stacks and placing it on the top of another stack
    - No disk may be placed on top of a smaller disk  
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

#### DIVIDE and CONQUER

Solve hard problems by breaking them into a set of sub-problems such that:
    - sub-problems are easier to solve than the original
    - solutions of the sub-problems can be combined to solve the original
1) palindrome.py

    test and show whether the input string is or not a palindrome
    an example of the divide and conquer algorithm


### Complete Programming Experience:polysum

A regular polygon has n number of sides. Each side has length s.<br>
The area of a regular polygon is:  <img src="https://latex.codecogs.com/gif.latex?\inline&space;\frac{0.25*n*s^2}{\tan(\pi&space;/n)}" title="\frac{0.25*n*s^2}{\tan(\pi /n)}" /><br>
The perimeter of a polygon is: length of the boundary of the polygon<br>
Write a function called `polysum` that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

#### Credit Card Problems
1) getRemainingBalance.py

    calculate the remaining balance at the end of the year, using the given balance, annulInterestRate, monthlyPaymentRate
2) getLowestPayment.py
    
    calculate the lowest fixed monthly payment(should be the multiple of ten) to pay off the balance within 12 months
3) getLowestPaymentBisection.py 

    use bisection search to fast the program


## | Structured Types
### 3.1 Tuples and Lists
#### TUPLE
1) Introdution
    - An ordered sequence of elements, can mix element types
    - ***immutable***, cannot change element values, cannot delete element(s) from the tuple, but can delete the whole tuple 
    - represented with parentheses, ***()***
    - any object split with comma defaults to a tuple `t=1,2 #type(t) -> tuple`
    
    ```python
    te = ()     # empty tuple
    to = (0,)   # tuple with one element
    t = (2,"one",3)
    t[0]        # evaluates to 2
    (2,"one",3) + (5,)      # evaluates to (2,"one",3,5)
    t[1:2]      # slice tuple, evaluates to ("one",)
    t[1] = 4    # gives error, can't modify object
    del(te)      # delete the empty tuple `te`
    ```

2) Operators
    ```python
    (1,) + (2,3)    # (1,2,3)
    ('hi',)*4       # ('hi','hi','hi','hi')
    3 in (1,2,3)    # True
    for e in (1,2,3)
    ```

>tuple can be used to exchange two elements very fast: `x,y = y,x` or `(x,y) = (y,x)`
and thus tuple can be used to return more than one objects: `return (a, b, c)`

3) Functions

    - ~~cmp(t1, t2)~~  in py3, import operator and use operator.lt(a, b) operator.le(a, b) operator.eq(a, b) operator.ne(a, b) operator.ge(a, b) operator.gt(a, b)
    Only available when elements of t1, t2 are the same type, if one of the length of a tuple is less than another, it's smaller(Assume the former elements are the same) 
    - len(t)
    - sum(t)   # (should all be int or float)
    - max(t)   # get the max element of the tuple  `t`
    - min(t)
    - tuple(seq)    # turn the list, dictionary, set `seq` to tuple, if `seq` is dictionary, return the tuple of keys

#### LIST
1) Introdution
    - ordered sequence of information, which means accessible by index
    - a list is denoted by square brackets, ***[]***
    - a list contains elements
     - usually homogeneous (i.e., all integers/all strings)
     - can contain mixed types(not common)
    - list is ***mutable***

    ```python
    le = []     # empty list
    l = [2,"one",3]
    l[0]        # evaluates to 2
    l[1:2]      # slice list, evaluates to ["one",]
    l[1] = 4    # list `l` turn out to be [2, 4, 3]
    l[2] + 2    # evaluate to 5

    - index can be a variable or expression, must evaluate to an int
    i = 2
    l[i-1]      # evaluate to 4, since l[1] is 4 from above
    ```

2) Operators
    ```python
    [1] + [2,3]    # [1,2,3]
    ['hi']*4       # ['hi','hi','hi','hi']
    3 in [1,2,3]   # True
    3 in [1,2,[3]] # False
    for e in [1,2,3]
    ```

3) Functions & Operations
    - len(l)
    - sum(l)   # (should all be int or float)
    - max(l)   # get the max element of the list  `l`
    - min(l)
    - list(seq)    # turn the tuple, dictionary, set `seq` to list, if `seq` is dictionary, return the list of keys

    ```python
    L = [1,2,5]
    L.append(7)    # list `L` turn out to be [1, 2, 5, 7]
    L.count(7)     # return the times that element 7 occurs in the list: 1
    L.extend(['new'])   # list `L` turn out to be [1, 2, 5, 7, 'new']
    L.index('new') # return 4, if `obj` is not in the list, gives error
    L.insert(0,'first') # list `L` turn out to be ['first', 1, 2, 5, 7, 'new']
    L.pop()        # default to remove the last element of the list, and return the removed element: 'new'
    L.pop(0)       # remove the element of index 0, thus return 'first'
    L.remove(7)    # remove the element 7, list `L` turn out to be [1, 2, 5]
    L.reverse()    # reverse the order of the list, list `L` turn out to be [5, 2, 1]
    L.sort()       # sort the elements of the list, list `L` turn out to be [1, 2, 5]
    sorted(L)      # sort the elements of the list, list `L` turn out to be [1, 2, 5] in the scope of global
    ```

### 3.2 Dictionaries and Sets
#### DICTIONARY
1) Introdution
    - store pairs of data (key : value)
    - a dictionary is denoted by curly braces, ***{}***
    - `key` of dictionary is ***immutable***(int,float,string,tuple,bool), since looking up the stored position of the `value` should depend on the hash value of the `key` ((actually need an hashable object, but think of as immutable as all immutable types are hashable)) **careful with float type as a key, might have an accuracy issue ||| careful with tuple type as a key, cause error when tuple contains mutable types**
    - `key` of dictionary is ***unique***, only the last `value` of the same `key` will be stored
    - `value` of dictionary can be any type(immutable or mutable), even other dictionaries
    - `value` of dictionary can be duplicates
    - ***no order*** to keys and values
    - can insert and search very fast, not impeding by the amount of keys, but take up lots of memory

    ```python
    dict = {}
    dict = {1: 'a', 2: 'b', 3: 'c'}
    dict[4] = 'd'   # add an entry
    dict[4] = 'ddd' # change the value of key 4
    del(dict[4])    # delete an entry
    del(dict)       # delete the dictionary
    ```

2) Operators
    ```python
    3 in {1:'a',3:'c'}      # True
    'a' in {1:'a',3:'c'}    # False
    for key in dict.keys:   # same as  for key in dict:
    for value in dict.values():
    for key, value in dict.items():
    ```

3) Functions & Operations
    - len(d)
    - sum(d)   # return the sum of the keys(should all be int or float)
    - str(d)   # output the string format of the dictionary d

    ```python
    d = {'a':'apple'}
    dict = {1: 'a', 2: 'b', 3: 'c', 9: [1,2]}
    d.clear()   # clear all the elements of the dictionary d, after that d is an empty dictionary
    dict.get(2) # 'b', get value from key
    dict.__contains__(2)    # True if 2 is one of the keys
    dict.items()    # dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (9, [1,2])]), return the list of tuple element that contains each key and value pair
    dict.keys() # dict_keys([1, 2, 3, 9])
    dict.values()   # dict_values(['a', 'b', 'c', [1, 2]])
    dict.setdefault(key, default=None)  # if key exists already, return the value; else if key not exist and no default value given, the new key's value will be None; else the new value will be the second parameter
    d2 = {4:'d'}
    dict.update(d2) # update the pair of key and value of d2 into dict
    pop_obj = dict.pop(4) # delete the item which key is 4, return the value of key 4: 'd', so pop_obj is 'd'
    pop_obj2 = dict.pop(6)  # if the key not exist, raise key error
    pop_obj3 = dict.pop(6, 'NotFound')  # if the key not exist, but has second parameter, then return the second parameter, so pop_obj3 is 'NotFound'
    dict.popitem()  # delete one random pair of key and value, and return it as a tuple, like (1, 'a')
    newdict = dict.fromkeys(seq[,value])    # create a new dictionary which has the same number of elements of dict, keys of newdict will be set as the seq given, seq can be list, tuple, dictionary, set; if the second parameter is empty, all the value of newdict will be None, else all will be the value
    
    # ---------
    # direct assignment & copy & deep copy
    # direct assignment: dict2 is dict -> True
    # copy: dict3 and dict are different objects, but their subobjects(like list) are point to the same object
    # deep copy: not only dict4 and dict are different objects, their subobjects are also point to different object(completely independent)

    import copy
    dict = {1: 'a', 2: 'b', 9: [1,2]}
    dic2 = dict
    dict3 = dict.copy()
    dict4 = copy.deepcopy(dict)
    
    dict[1] = 'aa'
    dict[4] = 'd'
    dict[9].append(4)

    print(dict)     # {1: 'aa', 2: 'b', 4: 'd', 9: [1,2,4]}
    print(dict2)    # {1: 'aa', 2: 'b', 4: 'd', 9: [1,2,4]}
    print(dict3)    # {1: 'a', 2: 'b', 9: [1,2,4]}
    print(dict4)    # {1: 'a', 2: 'b', 9: [1,2]}
    ```

4) biggest.py

    small practice to use dictionary


#### SET
1) Introdution
    - like dictionary, only stores keys
    - elements are all unique and not ordered
    - can do some set operations
    - using `set()` to generate a set from a list, tuple, dictionary, set, string

    ```python
    se = set()    # an empty set, print(se) -> set()
    s = set([1,2])  # print(s) -> {1,2}
    s1 = set((1,3)) # print(s1) -> {1,3}
    s2 = set({1: 'a', 4: 'd'})  # print(s2) -> {1,4}
    s3 = set('hello')   # print(s3) -> {'o','h','l','e'}
    ```

2) Operators
    ```python
    a = set([0,2,4,6,8])
    b = set([0,1,2,3,5,7])
    ab = a & b          # print(ab) -> {0,2}
    ab2 = a | b         # print(ab2) -> {0,1,2,3,4,5,6,7,8}
    ab3 = a - b         # print(ab3) -> {8,4,6}
    ab4 = a ^ b         # print(ab) -> {1,3,4,5,6,7,8}
    2 in set([1,2,3])   # True
    for i in set([1,2,3])
    ```

3) Functions & Operations
    - len(s)
    - sum(s)    # (should all be int or float)
    - set(seq)  # seq can be tuple, list, dictionary, set, string

    ```python
    s = set([0,2,4,6])
    s1 = set([0,1,2,3])

    s.add(8)
    s1.update([5,7,11,13])
    s1.remove(13)   # s1.remove(99) will raise an error
    s1.pop()    # remove one random element from s1, like elements are popped in the order they appear in the hash table, but its hash value can change
    s1.discard(11)  # like remove(), but won't raise error when element doesn't exist
    s1.issubset(s)  # False, return True if s1 is the subset of s
    ss = s.intersection(s1)     # same as  ss = s & s1
    ss2 = s.union(s1)           # same as  ss2 = s | s1
    ss3 = s.difference(s1)      # same as ss3 = s - s1
    ss4 = s.symmetric_difference(s1)    # same as ss4 = s ^ s1
    s.clear()   # after that, s is an empty set
    ```

1) hangman.py
    
    hangman game

## | Midterm Exam
1) closest_power.py

    return the closest power of base**power to num, in case of a tie, return the smaller value
2) deep_reverse.py

    reverse the elements of the list L which elements are also list and reverse the elements of each elements of the list L
3) isCharInStr_bisectionSearch_recursive.py

    use bisection search to tell whether or not the char is in the alphabetized string aStr    
4) score.py

    return the score of the word, which is the result of applying fuction f to the scores of the word's two highest scoring letter


## | Good Programming
### 4.1 Testing and Debugging
#### BLACK-BOX TESTING and GLASS-BOX TESTING

Black-box testing is a method of software testing that tests the ***functionality*** of an application. Recall from the lecture that a way to think about black-box testing is to look at both:

- The possible paths through the ***specification***.
- The possible ***boundary*** cases.
- Undoubtably many - if not all - of the listed tests look like they would be pretty good for testing the function size. However, we want you to think critically about the way size is specified - including possible boundary cases - and pick a set of tests that adequately and fully tests all paths and boundary conditions. Be sure the set of tests you pick does not have extraneous, useless, or repetitive tests.


A path-complete glass box test suite would find test cases that go through every possible path in the code. This is different from black-box testing, because in black-box testing you only have the function specification. For glass-box testing, you actually know how the function you are testing is defined. Thus you can use this definition to figure out how many different paths through the code exist, and then pick a test suite based on that knowledge.

#### BUGS
1) Runtime Bugs

    Overt vs. covert:<br>
    - ***Overt*** has an obvious manifestation - code crashes or runs forever
    - ***Covert*** has no obvious manifestation - code returns a value, which may be incorrect but hard to determine

    Persistent vs. intermittent:<br>
    - ***Persistent*** occurs every time code is run
    - ***Intermittent*** only occurs some  times, even if run on same input

2) Debugging

    - steep learning curve
    - goal is to have a bug-free program
    - tools
        - built in to IDE and Anaconda
        - Python Tutor
        - print statement
        - use your brain, be systematic in your hunt

    Logic Error(hard):
    - think before writing code
    - draw pictures, take break
    - explain code to some one else

    Steps:
    - study program code
        - ask how did I get the unexpected result
        - don't ask what is wrong
        - is it part of a family?
    - scientific method
        - study available data
        - form hypothesis
        - repeatable experiemnts
        - pick simplest input to test with
        
### 4.2 Exceptions and Assertions
#### EXCEPTIONS
1) Types
    
    Some types of exceptions: 
    - trying to access beyond list limits -> IndexError
    - using inexistent key of dictionary (dic['emp']) -> KeyError
    - referencing a non-existing variable, local or glabal name not found -> NameError
    - trying to convert an inappropriate type -> TypeError
    - mixing data types without coercion ( 'a'/4 ) -> TypeError
    - python can't parse program, trying to use keywords as a variable name -> SyntaxError
    - attribute reference fail, using inexistent attribute name of an object -> AttributeError
    - operand type okay, but value is illegal -> ValueError
    - IO system reports malfunction (e.g. file not found) -> IOError

2) What to do

    - fail silently: substitute default values or just continue; ***bad idea!*** cause user gets no warning
    - return an "error" value: complicates code have to check for a special value
    - stop execution, ***signal error*** condition: ***raise an exception***

3) Dealing with Exceptions
    ```python
    try:
        a = int(input("Tell me one number:"))
        b = int(input("Tell me another number:"))
        print(a/b)
        print("Okay")
    except:
        print("Bug in user input.")
        print("Outside")
    ```

    Handling specific exceptions:
    ```python
    try:
        a = int(input("Tell me one number:"))
        b = int(input("Tell me another number:"))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError:
        print("Could not convert to a number.")
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except:
        print("Something went very wrong.")
    ```

4) Other Exceptions

    - ***else***: body of this is executed when execution of associated ***try*** body completes with no exceptions
    - ***finally***: body of this is aleays executed after ***try***, ***else*** and ***except*** clauses, even if they raised another error or executed a ***break***, ***continue*** or ***return***  [useful for clean-up code that should be run no matter what else happened, like close a file]

5) Using Exceptions

    - ***raise***, control when to raise an exception by users, and program skips the next lines(same indentation): e.g. raise ValueError('error')
    see --> get_ratio.py

    ```python
    while True:
        try:
            n = input("Please enter an integer:")
            n = int(n)
            break
        except ValueError:
            print("Input not a integer; try again")
    print("Correct input of an integer~")
    ```

    ```python
    data = []
    file_name = input("Provide a name of a file of data")

    try:
        fh = open(file_name, 'r')
    except IOError:
        print('cannot open', file_name)
    else:
        for new in fh:
            if new != '\n':
                addIt = new[:-1].split(',') # remove trailing \n
                data.append(addIt)
    finally:
        fh.close() # close file even if fail

    gradeData = []
    if data:
        for student in data:
            try:
                name = student[0:-1]
                grades = int(student[-1])
                gradeData.append([name, [grades]])
            except ValueError:
                gradeData.append([student[:], []])
    ```

#### ASSERTIONS
1) Introduction
    
    - want to be sure that assumptions on state of computation are as expected
    - use an ***assert*** statement to raise an ***AssertionError*** exception if assumptions not met
    - an example of good defensive programming

    ```python
    def avg(grades): 
        '''
        Assumes: grades is a collection
        if the length of grades is 0, then throw out the message: no grades data;
        else return the average of the grades 
        '''
        assert not len(grades) == 0, 'no grades data'
        return sum(grades) / len(grades)
    ```

    - Features:
        - assertions don't allow a programmer to control response to unexpected conditions
        - ensure that execution ***halts*** whenever an expected condition isn't met
        - typically used to ***check inputs*** to functions procedures, but can be used anywhere
        - can be used to ***check outputs*** of a function to avoid propagaring bad values
        - can make it easier to locate a source of a bug

2) Where to use
    
    - goal is to spot bugs as soon as introduced and make clear where they happened
    - use as a supplement to ***testing***
    - ***raise exceptions*** if users supplies bad data input 
    - use assertions to
        - check ***types*** if arguments or values
        - check that ***invariants*** on data structures are met
        - check ***constraints*** on return values
        - check for ***violations*** of constraints on procedure(e.g. no duplicates in a list)

## | Object Oriented Programming
### 5.1 Classes and Inheritance

### 5.2 An Extended Example


## | Algorithmic Complexity
### 6.1 Computational Complexity

### 6.2 Searching and Sorting Algorithms


## | Plotting
### 7.1 Plotting
