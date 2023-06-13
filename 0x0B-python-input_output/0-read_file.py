#!/usr/bin/python3
"""Defines a function to read a text file and
   prints it to stdout
"""


def read_file(filename=""):
    """Reads a text file and prints it
       to stdout

       Args:
           filename: filename/path
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
