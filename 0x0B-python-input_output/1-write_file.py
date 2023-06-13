#!/usr/bin/python3
"""Defines a function to wrtie tot a file
   and returns the number of character writen
"""


def write_file(filename="", text=""):
    """writes string to a file

       Args:
           filename: filename/path
           text: string to be written

       Return:
             The number of character written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
