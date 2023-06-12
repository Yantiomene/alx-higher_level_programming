#!/usr/bin/python3
"""Defines a class that inheritated
   from list class
"""


class MyList(list):
    """Class that inheritated from list class
       with a public method
    """

    def print_sorted(self):
        """Prints a list in an ascending
           sorted order
        """
        list_cpy = self.copy()
        list_cpy.sort()
        print(list_cpy)
