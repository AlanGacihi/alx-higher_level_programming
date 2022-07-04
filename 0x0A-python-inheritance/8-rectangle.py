#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that defines a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializer for the rectangle class.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
