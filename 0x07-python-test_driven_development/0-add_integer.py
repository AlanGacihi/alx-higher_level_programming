#!/usr/bin/python3
"""Integer addition.

This module contains only one function to add two integers.

Example:
    add_integer(5, 2) should give the result 7.

"""


def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int: The addition of a and b.

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if a + 1 == a or b + 1 == b:
        raise OverflowError("Number too large")
    return int(a) + int(b)
