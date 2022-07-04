#!/usr/bin/python3
"""
This module contains the class Square.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Definition of a square
    """
    def __init__(self, size):
        """
        Initializer for the square class.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
