#!/usr/bin/python3
"""Rectangle.

Class that defines a rectangle with its width and height..

"""


class Rectangle:
    """Class that defines a rectangle with its width and height
    """
    def __init__(self, width=0, height=0):
        """The __init__ method uses a defaul width and height of 0.

        Args:
            width: Width for the rectangle.
            height: Height for the rectangle.
        Attributes:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
