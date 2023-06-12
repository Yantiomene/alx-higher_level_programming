#!/usr/bin/python3
"""Defines a fucntion to lookup the available
attribute and methods of an object
"""


def lookup(obj):
    """Lookup the availables attributes and
       methods of an object
       Args:
           obj: object
       Return:
             the list of attribute and method
    """

    return (dir(obj))
