#!/usr/bin/python3
"""Print square.

This module contains only one function that prints a square.

Example:
    print_square(2) should print:
    ##
    ##

"""


def print_square(size):
    """This function prints a square of a given size.

    Args:
        size (int): Desired size for the square.

    """

    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
    if (not size):
        print()
