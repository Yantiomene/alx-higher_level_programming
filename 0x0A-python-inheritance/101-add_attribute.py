#!/usr/bin/python3
"""Defines a method to set and attribute to an
   object if possible
"""


def add_attribute(mc, name, value):
    """Set and attribute to mc if possible

       Args:
           mc: class instance
           name: attribute name
           value: attribute value
    """
    if not hasattr(mc, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(mc, name, value)
