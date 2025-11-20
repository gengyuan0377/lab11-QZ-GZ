# https://github.com/gengyuanzhang317/lab11-QZ-GZ
# Partner 1: Gengyuan Zhang
# Partner 2: Qianfan Zeng


import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if not (a > 0 and a != 1 and b > 0):
        raise ValueError
    return math.log(b) / math.log(a)

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        if a < 0:
            raise ValueError("square_root() only defined for a >= 0")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("square_root() expects a number")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("hypotenuse() expects two numbers")