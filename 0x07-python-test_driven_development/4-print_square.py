#!/usr/bin/python3

"""
Defines a function to print a square with
the character #
"""


def print_square(size):
    """
       Prints a square wiht the character #
       Args:
           size: size of the square
       Returns:
              None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
