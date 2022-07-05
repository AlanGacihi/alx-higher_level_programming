#!/usr/bin/python3
"""
This module contains the function read_file.
"""


def read_file(filename=""):
    """
    Function that reads the contents of a file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
            print(f.read(), end="")
