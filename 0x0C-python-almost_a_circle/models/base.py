#!/usr/bin/python3
"""Package that contains the parent class of all
the sub classes that will be created later
"""


class Base:
    """Base class for all sub classes of the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
