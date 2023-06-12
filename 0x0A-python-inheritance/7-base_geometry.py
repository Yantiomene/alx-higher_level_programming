#!/usr/bin/python3
""" Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with a public class"""

    def area(self):
        """That raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

           Args:
               name: string
               value: int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
