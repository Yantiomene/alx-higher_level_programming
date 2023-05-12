#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
    else:
        for row in matrix:
            for i in row:
                if row.index(i) != (len(row) - 1):
                    print("{:d}".format(i), end=" ")
                else:
                    print("{:d}".format(i))
