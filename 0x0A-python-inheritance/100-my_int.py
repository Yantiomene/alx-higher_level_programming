#!/usr/bin/python3
"""Defines a class that inherits from int"""


class MyInt(int):
    """Inherits from int class"""

    def __eq__(self, other_int):
        """implement the __ne__ magic method"""
        return super().__ne__(other_int)

    def __ne__(self, other_int):
        """implement the __eq__ magic method"""
        return super().__eq__(other_int)
