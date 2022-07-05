#!/usr/bin/python3
"""
This module contains the function add_attribute.
"""


def add_attribute(cla, name, value):
    """
    Function that adds an attribute to a class, if possible.
    """
    if hasattr(cla, "__dict__"):
        cla.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
