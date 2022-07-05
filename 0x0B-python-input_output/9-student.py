#!/usr/bin/python3
"""
This module contains the class Student.
"""


class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializer for the new Student objects.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of a class.
        """
        return self.__dict__
