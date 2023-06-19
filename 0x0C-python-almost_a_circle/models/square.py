#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a square"""
        sq = "[Square] ({}) {}/{} - ".format(self.id, self.x, self.y)
        str_s = "{}".format(self.width)
        return (sq + str_s)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
