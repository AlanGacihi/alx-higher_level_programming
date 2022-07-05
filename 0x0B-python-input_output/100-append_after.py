#!/usr/bin/python3
"""
This module contains the function append_after.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that appends a string after another one found on a line.
    """
    with open(filename, "r", encoding='utf-8') as f:
        content = f.readlines()
    i = 0
    while i < len(content):
        if content[i].find(search_string) >= 0:
            i += 1
            content.insert(i, new_string)
        i += 1
    with open(filename, "w", encoding='utf-8') as f:
        f.writelines(content)
