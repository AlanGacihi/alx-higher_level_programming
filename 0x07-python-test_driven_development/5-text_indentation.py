#!/usr/bin/python3
"""Text indentation.

This module contains just one function that indents text.

Example:
    text_indentation("Hello. I'm Darwin")
    Should return:
    Hello.
    I'm Darwin
"""


def text_indentation(text):
    """Function that separates a text when a . ? or : is found.

    Args:
        text (str): Text to be formatted.
    """
    newline = 1
    spaces = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == ' ':
            spaces += 1
        elif char == '.' or char == '?' or char == ':':
            if not newline:
                print(" " * spaces, end="")
            print(char + "\n")
            newline = 1
        elif not newline:
            print(" " * spaces + char, end="")
            spaces = 0
        else:
            print(char, end="")
            newline = 0
            spaces = 0
