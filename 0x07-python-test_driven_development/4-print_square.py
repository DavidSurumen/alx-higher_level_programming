#!/usr/bin/python3
"""
This module defines a function `print_square`
that prints a square with '#'
"""


def print_square(size):
    """Prints a square of given size with '#'

    Args:
        size (integer): the size length of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    Returns:
        nothing
    """
    if size == "":
        raise ValueError('size is required')

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
