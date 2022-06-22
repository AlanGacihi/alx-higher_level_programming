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
            return self.__size ** 2

    @property
    def size(self):
        """Get size of square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
