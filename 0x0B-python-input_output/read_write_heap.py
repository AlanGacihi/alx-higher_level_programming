#!/usr/bin/python3
"""
This script replaces a string on the heap
"""


from sys import argv
if len(argv) != 4 or argv[3] == "" or argv[2] == "" or int(argv[1]) <= 0:
    print("Usage: ./read_write_heap.py pid search replace")
    exit(1)
maps = open('/proc/{}/maps'.format(argv[1]), 'r')
for line in maps:
    curr = line.split(' ')
    if curr[-1] != "[heap]\n":
        continue
    heap = curr[0].split('-')
    first = int(heap[0], 16)
    last = int(heap[1], 16)
    mem = open('/proc/{}/mem'.format(argv[1]), 'rb+')
    mem.seek(first)
    heap_mem = mem.read(last - first)
    offset = heap_mem.index(bytes(argv[2], "ASCII"))
    mem.seek(first + offset)
    mem.write(bytes(argv[3], "ASCII"))
    maps.close()
    mem.close()
    print("String modified!")
    break
