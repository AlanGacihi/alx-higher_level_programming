#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    if not roman_string:
        return 0

    conv = {"I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000}
    n = 0
    l = len(roman_string)
    i = 0

    while(i < l):
        if roman_string[i] == "I" and i != l - 1:
            if roman_string[i + 1] != "I":
                n += conv[roman_string[i + 1]] - 1
                i += 2
            else:
                n += conv[roman_string[i]]
                i += 1
        else:
            n += conv[roman_string[i]]
            i += 1

    return n
