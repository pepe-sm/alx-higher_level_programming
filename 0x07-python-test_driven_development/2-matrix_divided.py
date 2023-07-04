#!/usr/bin/python3
"""
    2-matrix_divided module
"""


def handle_errors(matrix, div):
    """ Handle errors in matrix and div inputs """

    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


def matrix_divided(matrix, div):
    """ Returns divided matrix """
    handle_errors(matrix, div)
    return [list(map(lambda n: round(n/div, 2), number)) for number in matrix]
