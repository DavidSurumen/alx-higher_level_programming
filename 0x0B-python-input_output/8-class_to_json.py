#!/usr/bin/python3
"""Contains a single function: 'class_to_json'"""


def class_to_json(obj):
    """Serializes a class object."""
    return obj.__dict__
