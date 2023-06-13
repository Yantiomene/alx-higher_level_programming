#!/usr/bin/pyhton3
"""Defines a function to returns a list of lists
   of integers representing the Pascal's trinagle of n
"""


def pascal_triangle(n):
    """Returns the Pascal's triangle

       Args:
           n: integer

       Return:
             The list os list of integer
    """
    if n <= 0:
        return []

    tri = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(tri[i - 1][j - 1] + tri[i - 1][j])
        row.append(1)
        tri.append(row)

    return tri
