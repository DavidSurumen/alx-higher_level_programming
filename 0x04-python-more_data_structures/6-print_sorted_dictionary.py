#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    sort = dict(sorted(a_dictionary.items()))
    for key, val in sort.items():
        print(key, ':', val)
