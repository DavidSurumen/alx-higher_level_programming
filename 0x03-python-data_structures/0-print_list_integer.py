#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        print('[]')
    else:
        for i in my_list:
            print("{}".format(i))
