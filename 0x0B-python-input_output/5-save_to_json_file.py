#!/usr/bin/python3
"""
This module contains the function save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that saves the json representation of an object in a file.
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
