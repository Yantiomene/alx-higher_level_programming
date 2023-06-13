#!/usr/bin/python3
"""Defines a function to wrtie an object to a text file
   using a JSON representation of the object
"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using using JSON

       Args:
           my_obj: Python object
           filename: filename/path
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
