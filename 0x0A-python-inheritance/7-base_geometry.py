#!/usr/bin/python3
"""
This module contains the class BaseGeometry.
"""


class BaseGeometry:
    """
    Class that defines basic geometries.
    """
    def area(self):
        """
        Area of a geometry, not implemented by default.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates that value is integer.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
