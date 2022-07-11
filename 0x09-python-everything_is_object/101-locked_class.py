#!/usr/bin/python3
"""Module 101-locked_class
defines a class 'LockedClass'
"""


class LockedClass(object):
    """
    Class that can only have one attribute, 'first_name'
    """
    __slots__ = ['first_name']
