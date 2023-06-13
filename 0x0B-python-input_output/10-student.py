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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student"""

        res = self.__dict__

        if type(attrs) is list:
            for at in attrs:
                if type(at) is not str:
                    return res

            at_dict = {}
            for at in attrs:
                for d in res:
                    if at == d:
                        at_dict[at] = res[at]

            return at_dict

        return res
