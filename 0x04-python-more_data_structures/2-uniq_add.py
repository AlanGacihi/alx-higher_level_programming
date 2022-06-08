#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    my_list = list(dict.fromkeys(my_list))
    return sum(my_list)
