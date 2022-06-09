#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    for k in sorted(a_dictionary.keys()):
        print("{}: {}".format(k, a_dictionary[k]))
