#!/usr/bin/python3
from sys import argv


argc = len(argv)
if argc != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(argv[1])
except Exception as e:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
tested = [-1] * N
i = 0
while i < N and i >= 0:
    j = tested[i] + 1
    while j < N:
        k = 0
        while k < i:
            if tested[k] == j or abs(tested[k] - j) == abs(k - i):
                break
            k += 1
        if k == i:
            tested[i] = j
            break
        j += 1
    if j == N:
        tested[i] = -1
        i -= 2
    i += 1
    if i == N:
        i -= 1
        print([[d, tested[d]]for d in range(N)])
