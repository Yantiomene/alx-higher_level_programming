#!/usr/bin/python3
"""Defines a class with no attribue or no class
   that prevents the user from dynamically creating
   new instance
"""


class LockedClass:
    """LockedClass prevents user for dynamically
       creating new instance
    """
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
