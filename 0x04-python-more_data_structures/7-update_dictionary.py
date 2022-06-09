#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    add = {key: value}
    a_dictionary.update(add)
    return a_dictionary
