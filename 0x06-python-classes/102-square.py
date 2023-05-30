#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """Defines a square with size private attibute
    a size property, a property setter and an area
    method"""
    def __init__(self, size=0):
        """Initialize the size"""
        self.size = size

    @property
    def size(self):
        """Method to retrieve the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """equal signe"""
        return (self.__size ** 2 == other.__size ** 2)

    def __ne__(self, other):
        """ not equal sign"""
        return (self.__size ** 2 != other.__size ** 2)

    def __lt__(self, other):
        """ less than sign"""
        return (self.__size ** 2 < other.__size ** 2)

    def __le__(self, other):
        """ less or equal sign"""
        return (self.__size ** 2 <= other.__size ** 2)

    def __gt__(self, other):
        """ greater than sign """
        return (self.__size ** 2 > other.__size ** 2)

    def __ge__(self, other):
        """ greater or equal sign"""
        return (self.__size ** 2 >= other.size ** 2)
