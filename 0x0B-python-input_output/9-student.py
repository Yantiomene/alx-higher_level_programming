#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Student class with 3 publics attributes

       Attr:
           first_name: public attr
           last_name: public attr
           age: public attr

       Method:
             to_json: public method
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the attibutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a student"""
        return self.__dict__
