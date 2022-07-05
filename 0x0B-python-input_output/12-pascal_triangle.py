#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    pasc = [[1]]
    row = []
    for i in range(n - 1):
        for j in range(len(pasc[i]) + 1):
            if j == 0 or j == len(pasc[i]):
                row.append(1)
            else:
                row.append(pasc[i][j - 1] + pasc[i][j])
        pasc.append(row[:])
        row.clear()
    return pasc
