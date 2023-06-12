#!/usr/bin/python3
"""defines a fucntion that check if
   an instance belong to a class or it subclass
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class
       or it subclass

       Args:
           obj: object
           a_class: a class

       Return:
             True or False
    """
    return isinstance(obj, a_class)
