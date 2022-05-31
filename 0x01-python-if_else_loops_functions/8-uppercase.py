#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{}".format(str[i] if ord(str[i]) < 97 or ord(str[i]) >
                          123 else chr(ord(str[i]) - 32)), end="")
    print()
