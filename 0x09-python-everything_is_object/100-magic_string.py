#!/usr/bin/python3
def magic_string():
    vars(magic_string).setdefault('my', []).append("Holberton")
    return ", ".join(magic_string.my)
