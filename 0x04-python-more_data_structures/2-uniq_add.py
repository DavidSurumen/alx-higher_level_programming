#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    new = set(my_list)
    add = 0
    for i in new:
        add += i
    return add
