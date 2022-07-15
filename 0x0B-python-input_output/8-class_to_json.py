#!/usr/bin/python3
"""Contains a single function: 'class_to_json'
"""
import json


def class_to_json(obj):
    """Serializes an object."""
    return obj.__dict__
