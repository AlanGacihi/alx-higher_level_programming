#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = ["+", "-", "*", "/"]
    if argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {} {:d} = {:d}".format(a, argv[2], b,
                                       add(a, b) if argv[2] == '+' else
                                       sub(a, b) if argv[2] == '-' else
                                       mul(a, b) if argv[2] == '*' else
                                       div(a, b)))
