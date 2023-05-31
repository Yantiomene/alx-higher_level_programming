#!/usr/bin/python3

"""Magic class to define a circle object"""


class MagicClass:
    """ Magic class that create a circle and evalute
    it area and circumference"""
    def __init__(self, radius=0):
        """initialize the radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
        return (None)

    def area(self):
        """evaluate the area of the circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """evaluate the circumference of the circle"""
        return (2 * math.pi * self.__radius)
