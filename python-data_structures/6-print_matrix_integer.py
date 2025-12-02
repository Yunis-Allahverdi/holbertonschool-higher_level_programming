#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new_matrix = [[[x[i] for x in matrix] for i in range(3)]]
    return '{:d}'.format(new_matrix)


matrix = [[]]
