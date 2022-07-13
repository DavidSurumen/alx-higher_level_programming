#!/usr/bin/python3
"""Module '101-add_attribute' contains only
one function.
"""


def add_attribute(obj, key, value):
    """Function that adds a new attribute to an object,
    if it is possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
