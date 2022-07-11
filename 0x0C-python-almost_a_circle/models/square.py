#!/usr/bin/python3
"""
This module contains the class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the square.
        """
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" +\
               str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """
        Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Function to update a square.
        """
        if args != ():
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Function that returns the dictionary representation of a square.
        """
        new = dict()
        for key in self.__dict__.keys():
            if key in ["_Rectangle__height", "_Rectangle__width"]:
                new["size"] = self.__dict__[key]
                continue
            new[key.split("_")[-1]] = self.__dict__[key]
        return new
