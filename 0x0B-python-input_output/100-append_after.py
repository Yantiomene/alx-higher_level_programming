#!/usr/bin/python3
"""Defines a function to insert a line after a line
   containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file after each
       line containing a specif string

       Args:
           filename: filename
           search_string: string to search
           new_string: new string to be inserted
    """
    list_line = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            list_line.append(line)
            if line.find(search_string) != -1:
                list_line.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(list_line)
