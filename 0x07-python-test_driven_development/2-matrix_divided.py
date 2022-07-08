#!/usr/bin/python3
"""
This module defines a function that divides all elements of
a matrix by a divisor
"""


def matrix_divided(matrix, div):
    """divides each element of a matrix by div

    Args:
        matrix (list): matrix to divide
        div (int): divisor

    Raises:
        TypeError: div must be a number
        TypeError: each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        ZeroDivisionError

    Returns:
        lists: matrix divided by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div < 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
            )

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = [x[:] for x in matrix]

    for line in new_matrix:
        if len(line) != len(new_matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        for index, elem in enumerate(line):
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                        )
            line[index] = round(elem/div, 2)
    return new_matrix
