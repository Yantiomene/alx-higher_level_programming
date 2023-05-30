#!/usr/bin/python3

""" Module that defines a class with a private
instance attribute size"""


class Square:
    """Define a square with a size private
    instance attribute"""

    def __init__(self, size):
        """ Initialize the instance of square
        with a size"""
        self.__size = size
