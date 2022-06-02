#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    print("{:d} {}{}".format(argc, "argument" if argc == 1 else "arguments",
                             ":" if argc else "."))
    for i in range(argc):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
