#!/usr/bin/python3
"""
This module contains the function number_of_lines.
"""


def number_of_lines(filename=""):
    """
    Function that returns the number of lines on a file.
    """
    lines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
