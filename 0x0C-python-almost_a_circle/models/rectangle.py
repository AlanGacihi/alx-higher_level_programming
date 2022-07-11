#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class that defines a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        X coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Y coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Function that returns the area of a rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Function that displays a rectangle using #
        """
        y_pos = "\n" * self.__y
        rect = (" " * self.__x + "#" * self.__width + "\n") * self.__height
        print(y_pos + rect[:-1])

    def __str__(self):
        """
        String representation of the rectangle.
        """
        return "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/" +\
               str(self.__y) + " - " + str(self.__width) + "/" +\
               str(self.__height)

    def update(self, *args, **kwargs):
        """
        Function to update a rectangle.
        """
        if args != ():
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Function that returns the dictionary representation of a rectangle.
        """
        new = dict()
        for key in self.__dict__.keys():
            new[key.split("_")[-1]] = self.__dict__[key]
        return new
