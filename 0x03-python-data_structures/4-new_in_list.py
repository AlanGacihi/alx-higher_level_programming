#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = list.copy(my_list)
    if idx >= 0 and idx < len(my_list):
        new[idx] = element
    return newx
