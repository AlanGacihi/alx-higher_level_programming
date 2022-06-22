#!/usr/bin/python3

"""Square"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
        size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of a square"""
        return self.__size ** 2
