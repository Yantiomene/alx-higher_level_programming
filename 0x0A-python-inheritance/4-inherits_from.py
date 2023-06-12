#!/usr/bin/python3
"""defines a fucntion that checks if
   an object is an instance of a class that inherited
   from the specified class
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class
       that inherited from a specified class

       Args:
           obj: object
           a_class: a class

       Return:
             True or False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
