#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    for i in matrix:
        print(' '.join('{0}'.format(element) for element in i))
