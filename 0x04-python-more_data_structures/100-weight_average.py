#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    avg = 0
    size = 0
    for tup in my_list:
        avg += tup[0] * tup[1]
        size += tup[1]

    return avg / size
