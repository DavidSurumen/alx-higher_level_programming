#!/usr/bin/python3
"""Defines a single function: 'append_after'
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.
    """
    new_lines = ""

    with open(filename, 'r', encoding='UTF-8') as f:
        content = f.readline()
        while content:
            new_lines += content
            if search_string in content:
                new_lines += new_string
            content = f.readline()

    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(new_lines)
