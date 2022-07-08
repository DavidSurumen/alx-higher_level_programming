#!/usr/bin/python3
"""
This module defines a function ``text_indentation``
that prints a text with 2 new lines after '.', '?', and
':'.
"""


def text_indentation(text):
    """prints a given text, with 2 new lines after each of these characters:
        '.', '?', and ':'.

    Args:
        text (string): the text to print

    Raises:
        TypeError: text must be a string

    Returns:
        nothing
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    delims = ['.', '?', ':']
    flag = False

    for c in text:
        if c.isspace() and flag is False:
            continue
        elif c in delims:
            print("{}\n\n".format(c), end="")
            flag = False
            continue
        else:
            print("{}".format(c), end="")
            flag = True
