#!/usr/bin/python3

"""Square"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return self.__size ** 2

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
