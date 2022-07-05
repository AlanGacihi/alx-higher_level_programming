#!/usr/bin/python3
"""
This module contains the function from_json_string.
"""
import json


def from_json_string(my_str):
    """
    Function that returns the object represented by a json string.
    """
    return json.loads(my_str)
