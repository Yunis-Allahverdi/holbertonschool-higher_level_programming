#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new_matrix = [[[x[i] for x in range(3)] for i in matrix]]
    return '{:d}'.format(new_matrix)


matrix = [[]]
