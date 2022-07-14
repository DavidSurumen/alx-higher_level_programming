#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then save them to a file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    args_list = []
    argv.pop(0)

    for elem in argv:
        args_list.append(elem)
    try:
        deserialized = load_from_json_file("add_item.json")
        deserialized.extend(args_list)

        save_to_json_file(deserialized, "add_item.json")

    except FileNotFoundError:
        save_to_json_file(args_list, "add_item.json")
