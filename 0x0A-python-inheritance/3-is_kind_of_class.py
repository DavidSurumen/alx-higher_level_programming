#!/usr/bin/python3
"""
Module '3-is_kind_of_class' defines a single
function 'is_kind_of_class'
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of the given class,
    or an instance of one of the base classes
    """
    if isinstance(obj, a_class):
        return True
    return False
