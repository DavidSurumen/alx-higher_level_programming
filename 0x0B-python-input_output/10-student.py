#!/usr/bin/python3
"""Defines a single class: 'Student'"""


class Student:
    """Class Student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a
        Student instance.
        """
        if type(attrs) is list and all(isinstance(x, str) for x in attrs):
            sub = {k: v for k, v in self.__dict__.items() if k in attrs}
            return sub
        return self.__dict__
