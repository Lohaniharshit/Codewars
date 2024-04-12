'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''
##
def zero(a=None):
    if a:
        return eval('0'+a)
    else:
        return '0'
def one(a=None):
    if a:
        return eval('1'+a)
    else:
        return '1'
def two(a=None):
    if a:
        return eval('2'+a)
    else:
        return '2'
def three(a=None):
    if a:
        return eval('3'+a)
    else:
        return '3'
def four(a=None):  
    if a:
        return eval('4'+a)
    else:
        return '4'
def five(a=None):
    if a:
        return eval('5'+a)
    else:
        return '5'
def six(a=None):  
    if a:
        return eval('6'+a)
    else:
        return '6'
def seven(a=None):
    if a:
        return eval('7'+a)
    else:
        return '7'
def eight(a=None):
    if a:
        return eval('8'+a)
    else:
        return '8'
def nine(a=None):
    if a:
        return eval('9'+a)
    else:
        return '9'
 
def plus(a): return '+'+a
def minus(a): return '-'+a
def times(a): return '*'+a
def divided_by(a): return '//'+a
 
print(seven(times(five())))

(seven(times(five())))