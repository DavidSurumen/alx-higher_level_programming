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
        json_list = []

        if list_objs is None:
            pass
        else:
            objs_dicts = []
            for i in list_objs:
                objs_dicts.append(i.to_dictionary())

            json_list.append(cls.to_json_string(objs_dicts))
            
            filename = "{}.json".format(cls.__name__)

        with open(filename, 'w', encoding='UTF-8') as f:
            for elem in json_list:
                f.write(elem)

