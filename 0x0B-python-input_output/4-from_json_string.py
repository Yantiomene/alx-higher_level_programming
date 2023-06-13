#!/usr/bin/python3
"""Defines a function that returns an
   object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns an object from a JSON string

       Args:
           my_str: a JSON str

       Return:
             a Python object
    """
    return json.loads(my_str)
