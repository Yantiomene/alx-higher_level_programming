#!/usr/bin/python3
"""Defines a function that returns the dictionary description
   with simple data structure for a JSON
"""


def class_to_json(obj):
    """Returns the dictionary description

       Args:
           obj:a python object

       Return:
             The dict decription
    """
    dict_des = {}
    if hasattr(obj, '__dict__'):
        dict_des = obj.__dict__
    return dict_des
