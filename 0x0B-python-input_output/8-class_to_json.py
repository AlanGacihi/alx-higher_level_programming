#!/usr/bin/python3
"""
This module contains the function class_to_json.
"""


def class_to_json(obj):
    """
    Function that returns dictionary description.
    """
    return obj.__dict__
