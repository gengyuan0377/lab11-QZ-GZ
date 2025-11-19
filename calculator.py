"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a==0:
        raise ZeroDivisionError
    return b/a
def log(a,b):
    if not (a>0 and a!=1 and b>0):
        raise ValueError
    return math.log(b)/math.log(a)
def exp(a, b):
    return a^b

