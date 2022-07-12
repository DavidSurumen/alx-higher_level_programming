#!/usr/bin/python3
"""
Module '1-my_list'
Defines a class 'MyList' that inherits from 'list'
"""


class MyList(list):
    """Class MyList that inherits the 'list' class
    """
    def print_sorted(self):
        """prints the list, sorted in ascending order
        Assumption: all elements of the list are of type int
        """
        print(sorted(self))
