#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, div, mul

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = ['+', '*', '-', '/']
    if argv[2] not in operators:
        print("Unkown operator. Available operators: +, -, *, and /")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])

    if argv[2] == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))

    elif argv[2] == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))

    elif argv[2] == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))

    else:
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
