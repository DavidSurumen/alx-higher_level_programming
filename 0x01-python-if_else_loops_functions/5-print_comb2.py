#!/usr/bin/python3
x = 0
for i in range(100):
    if i // 10 == 0:
        print("0", end="")
    print("{}".format(i), end=", " if i < 99 else "\n")
