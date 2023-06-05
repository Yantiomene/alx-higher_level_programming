#!/usr/bin/python3
"""Defines a Rectangle class
"""


class Rectangle:
    """Define a rectangle
       attr:
           width: positive integer (private)
           height: positive integer (private)
           number_of_instances: positive integer (public)
           print_symbol: any type (public)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a new instance of the rectangle
           Args:
               width: width
               height: height
           Returns:
                  None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves the width
           Returns:
                  width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the value of the width
           Args:
               value: value to be set
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height
           Returns:
                  height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the value fo the heigth
           Args:
               value: value to be set
           Returns:
                  None
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """evaluate the area of the rectangle
           Returns:
                  area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Evaluate the perimeter of the rectangle
           Returns:
                  perimiter
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """get the string representation of a rectangle
           Returns:
                  string with print_symbol attribute
        """

        rect = ""

        if self.__height == 0 or self.width == 0:
            return (rect)
        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width + '\n'

        return (rect[:-1])

    def __repr__(self):
        """get the string representation of a rectangle
           object
           Return:
                 that string representation
        """

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Called when a rectangle object is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
