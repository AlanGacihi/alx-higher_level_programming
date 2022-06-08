#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    for key, val in dict(a_dictionary).items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
