#!/usr/bin/python3
"""
This module contains the function load_from_json.
"""
import json


def load_from_json_file(filename):
    """
    Function that loads an object from a json file.
    """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
