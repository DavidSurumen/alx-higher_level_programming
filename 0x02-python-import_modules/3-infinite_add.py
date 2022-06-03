#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    res = 0
    for i in range(len(argv)):
        if i == 0:
            continue
        res += int(argv[i])
    print(res)
