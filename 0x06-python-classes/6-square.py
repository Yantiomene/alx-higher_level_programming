#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """Defines a square with size and position
    private attibute, getter and setter properties
    and an area and my_print methods"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size and the position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the value of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
