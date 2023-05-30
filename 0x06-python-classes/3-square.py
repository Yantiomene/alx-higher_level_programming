#!/usr/bin/python3

"""Defines a class of the Square"""


class Square:
    """Defines a square with a size and
    a method for to calculate the area"""
    def __init__(self, size=0):
        """Initialize the size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
