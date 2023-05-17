#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers of a matrix
    Args:
        matrix: 2 dimensional matrix
    Return:
        a new matrix of the same size where
        each value is a square of the value of the input
    '''
    new_matrix = [[i ** 2 for i in row] for row in matrix]
    return (new_matrix)
