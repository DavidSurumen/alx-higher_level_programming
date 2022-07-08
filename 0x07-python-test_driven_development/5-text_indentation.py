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

    new_text = ""
    flag = False

    for index, char in  enumerate(text):
        if flag == False:
            new_text += char
        else:
            flag = False
        if char == '.' or char == '?' or char == ':':
            new_text += '\n\n'
            flag = True

    print(new_text)
