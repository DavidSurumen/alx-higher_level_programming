#!/usr/bin/python3
"""Contains a single class: 'Base'"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
