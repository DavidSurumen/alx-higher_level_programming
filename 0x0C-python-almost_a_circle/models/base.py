#!/usr/bin/python3
"""Contains a single class: 'Base'"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""

        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, 'r', encoding='UTF-8') as f:
                json_str = f.read()
        except FileNotFoundError:
            return []

        dict_list = cls.from_json_string(json_str)
        instances = [cls.create(**instances) for instances in dict_list]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV."""
        filename = '{}.csv'.format(cls.__name__)
        dict_list = [ls.to_dictionary() for ls in list_objs]
        if len(dict_list) != 0:
            header = dict_list[0].keys()        

            with open(filename, 'w', encoding='UTF-8') as fp:
                writer = csv.DictWriter(fp, fieldnames=header)
                writer.writeheader()
                for data in dict_list:
                    writer.writerow(data)
        else:
            header = []
            with open(filename, 'w', encoding='UTF-8') as fp:
                f.write(header)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes CSV."""
        filename = '{}.csv'.format(cls.__name__)
        obj_list = []

        with open(filename, 'r', encoding='UTF-8') as fp:
            header = fp.readline().replace('\n', '').split(',')
            for el in fp.readlines():
                val = map(int, el.replace('\n', '').split(','))
                data = dict(zip(header, val))
                obj_list.append(cls.create(**data))

        return obj_list
