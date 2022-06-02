#!/usr/bin/python3

for i in range(10):
    for x in range(10):
        if i < x:
            if int(str(i) + str(x)) < 89:
                print("{}{}".format(i, x), end=", ")
            else:
                print("{}{}".format(i, x), end="\n")
        else:
            continue
