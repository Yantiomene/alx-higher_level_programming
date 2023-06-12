#!/usr/bin/python3
"""defines a fucntion that check if
   an instance belong to a class
"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class

       Args:
           obj: object
           a_class: a class

       Return:
             True or False
    """
    return type(obj) is a_class
