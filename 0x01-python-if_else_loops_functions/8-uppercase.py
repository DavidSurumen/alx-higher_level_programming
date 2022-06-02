#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < 97:
            print(str[i], end="" if i+1 < len(str) else "\n")
        else:
            print("{}".format(chr(ord(str[i]) - 32)), end="" if i+1 < len(str) else "\n")
