#!/usr/bin/python3
"""Contains a single class: 'Base'"""


class Base:
    """Base class containing private class attribute
    'nb_objects',
    and constructor method'"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class contructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
