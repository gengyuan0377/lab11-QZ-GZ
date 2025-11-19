"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    try:
        if a<0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as e:
        print(e)
        return None
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError as e:
        print(e)
        return None
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a==0:
        raise ZeroDivisionError
    return b/a
def logarithm(a,b):
    if not (a>0 and a!=1 and b>0):
        raise ValueError
    return math.log(b)/math.log(a)
def exponent(a, b):
    return a^b

