#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    return [i if i != search else replace for i in my_list]
