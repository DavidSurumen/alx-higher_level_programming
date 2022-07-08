#!/usr/bin/python3
"""
This module defines a function that prints
your name
"""


def say_my_name(first_name, last_name=""):
    """Prints back your name

    Args:
        first_name (string): first name. Required
        last_name (string): optional

    Raises:
        TypeError: first_name and last_name must be strings

    Returns:
        nothing
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if first_name == "":
        raise ValueError('first_name is required')

    print('My name is ' + first_name + ' ' + last_name)
