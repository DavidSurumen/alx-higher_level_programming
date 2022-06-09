#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    new_matrix = []
    for line in matrix:
        new_matrix.append([i**2 for i in line])
    return new_matrix
