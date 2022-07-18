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
        """takes a list of dictionaries and
        returns a list of the JSON string representation."""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """takes a list of objects, and writes
        the JSON string representation to a file."""

        if list_objs is None:
            objs_dicts = []
        else:
            objs_dicts = [i.to_dictionary() for i in list_objs]

        json_string = cls.to_json_string(objs_dicts)
        filename = "{}.json".format(cls.__name__)

        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """takes a JSON representation string, and returns the list.
        'json_string' is a string representing a list of dictionaries.
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
