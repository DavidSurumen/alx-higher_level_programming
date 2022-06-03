#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{} arguments.".format(0))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv)-1))
        print("{}: {}".format(len(argv)-1, argv[len(argv)-1]))
    else:
        print("{} arguments:".format(len(argv)-1))
        for i in range(len(argv)):
            if i == 0:
                continue
            print("{}: {}".format(i, argv[i]))
