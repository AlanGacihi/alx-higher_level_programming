#!/usr/bin/python3
"""
This module contains the class is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Function that tells if the obj is exactly an instance of a_class.
    """
    if type(obj) is a_class:
        return True
    return False
