#!/usr/bin/python3

"""Defines a function to add 2 numbers"""


def add_integer(a, b=98):
    """
    Adds 2 integers

    Args:
       a: first number
       b: second number with a default value of 98

    Returns:
       The sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
