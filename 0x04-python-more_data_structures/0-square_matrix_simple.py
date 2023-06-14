#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    bidimensional_matrix = []
    for element in matrix:
        bidimensional_matrix.append(list(map(lambda i: i**2, element)))
    return bidimensional_matrix
