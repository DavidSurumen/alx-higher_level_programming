#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, div, mul

    if len(argv)-1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = ['+', '*', '-', '/']
    if argv[2] not in operators:
        print("Unkown operator. Available operators: +, -, *, and /")
        exit(1)

    argv1 = int(argv[1])
    argv3 = int(argv[3])

    if argv[2] == '+':
        print("{} + {} = {}".format(argv1, argv3, add(argv1, argv3)))

    elif argv[2] == '-':
        print("{} - {} = {}".format(argv1, argv3, sub(argv1, argv3)))

    elif argv[2] == '*':
        print("{} * {} = {}".format(argv1, argv3, mul(argv1, argv3)))
    
    else:
        print("{} / {} = {}".format(argv1, argv3, div(argv1, argv3)))
