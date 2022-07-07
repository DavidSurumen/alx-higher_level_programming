#!/usr/bin/python3
"""
This is a function that adds two integers.
It two arguments which must be of type integer, and
returns their sum
"""


def add_integer(a, b=98):
    """returns the sum of two integers.
    all args must be integers, or casted to integers if they are float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
