#!/usr/bin/python3
"""Defines a class that inherited from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherited from Rectangle"""

    def __init__(self, size):
        """Initialised the private attribute"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """return the area of the square"""
        return super().area()

    def __str__(self):
        """Returns a string representation of a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
