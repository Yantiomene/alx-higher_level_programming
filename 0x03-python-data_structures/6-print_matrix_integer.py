#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or len(matrix) == 0 or len(matrix) == 1:
        print()
    else:
        for row in matrix:
            for i in range(len(row)):
                if i < (len(row) - 1):
                    print("{:d}".format(row[i]), end=" ")
                else:
                    print("{:d}".format(row[i]))
