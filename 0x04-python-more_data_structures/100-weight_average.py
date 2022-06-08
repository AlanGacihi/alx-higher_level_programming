#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = sum([v * w for v, w in my_list])
    d = sum([w for v, w in my_list])
    if not d:
        return 0
    return n/d
