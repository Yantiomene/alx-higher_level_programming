#!/usr/bin/python3

"""Module that defines a Square class"""


class Square:
    """Defines a Square with a size attribute
    and a validation on the size"""

    def __init__(self, size=0):
        """Initialize the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
