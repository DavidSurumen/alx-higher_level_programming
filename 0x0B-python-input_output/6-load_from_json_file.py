#!/usr/bin/python3
"""Contains a single function: 'load_from_json_file'
"""
import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file"
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.load(f)
