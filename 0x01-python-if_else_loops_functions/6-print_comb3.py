#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i >= j or (i == 8 and j == 9):
            continue
        print("{:d}{:d}".format(i, j), end=', ')
print('{:d}'.format(89))
