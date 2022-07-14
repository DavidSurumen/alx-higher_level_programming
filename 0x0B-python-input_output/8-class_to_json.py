#!/usr/bin/python3
"""Contains a single function: 'class_to_json'
"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple
    data structure (list, dictionary, string, integer,
    and boolean) for JSON serialization of an object.
    """
    obj_js = json.dumps(obj.__dict__)
    return json.loads(obj_js)
