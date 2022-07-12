#!/usr/bin/python3
"""
Module `0-lookup`.
Defines a function 'lookup(obj)'
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj : object
    """
    return dir(obj)
