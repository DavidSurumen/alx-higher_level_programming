#!/usr/bin/python3
"""Module '0-read_file' defines a single
function: 'read_file'
"""


def read_file(filename=""):
    """reads a text file, and prints it to stdout.
    """
    with open(filename, encoding='UTF-8') as f:
        data = f.read()
    print(data)