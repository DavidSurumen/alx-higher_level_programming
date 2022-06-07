#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    newl = [n % 2 == 0 for n in my_list]
    return newl
