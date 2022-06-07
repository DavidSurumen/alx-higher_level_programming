#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for col in line:
            print("{:d}".format(col), end=" " if line.index(col)+1 < len(line) else "")
        print()
