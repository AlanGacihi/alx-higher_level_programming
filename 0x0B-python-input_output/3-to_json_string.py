#!/usr/bin/python3
"""
This module contains the function to_json_string.
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the json representation of an object.
    """
    return json.dumps(my_obj)
