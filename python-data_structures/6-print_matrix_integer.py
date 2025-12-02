#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(3):
        for y in range(3):
            print("{:d}".format(matrix[x][y]), end=" ")

        print("{}".format("\n"))


matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
print_matrix_integer(matrix)
