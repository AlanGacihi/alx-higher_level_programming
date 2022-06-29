#!/usr/bin/python3
"""Say my name.

This module contains one function to print a name.

Example:
    say_my_name("Julien", "Barbier")
        should print My name is Julien Barbier

"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first_name> [<last_name>].

    Args:
        first_name (str): First name to be printed.
        last_name (str): Optional. Lastname to be printed.

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name, end="")
    if last_name is not "":
        print(" ", end="")
    print(last_name)
