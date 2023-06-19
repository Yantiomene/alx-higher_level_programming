#!/usr/bin/python3
"""Package that contains the parent class of all
the sub classes that will be created later
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
