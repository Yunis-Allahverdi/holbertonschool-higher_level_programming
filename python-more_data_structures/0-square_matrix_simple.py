#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row] for row in matrix]
    return [[x for x in row] for row in matrix]


matrix = [[]]
square_matrix_simple(matrix)
