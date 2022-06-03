#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for elem in my_list:
        result.append(True if not elem % 2 else False)
    return result
