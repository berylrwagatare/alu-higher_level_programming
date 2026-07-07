#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        elements = [ "{:d}".format(n) for n in row ]
        print(" ".join(elements))
