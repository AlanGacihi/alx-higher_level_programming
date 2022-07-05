#!/usr/bin/python3
"""
This module contains the class MyInt.
"""


class MyInt(int):
    """
    Own class that inherits from int.
    """
    def __eq__(self, other):
        """
        Function that handles equality.
        """
        if int(self) == int(other):
            return False
        return True

    def __ne__(self, other):
        """
        Function that handles inequality.
        """
        return not self.__eq__(other)
