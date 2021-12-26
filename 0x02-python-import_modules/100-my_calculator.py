#!/usr/bin/python3
from sys import setswitchinterval


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sing = sys.argv[2]
    if sing == '+':
        print("{} {} {} = {}".format(a, sing, b, add(a, b)))
    elif sing == '-':
        print("{} {} {} = {}".format(a, sing, b, sub(a, b)))
    elif sing == '*':
        print("{} {} {} = {}".format(a, sing, b, mul(a, b)))
    elif sing == '/':
        print("{} {} {} = {}".format(a, sing, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
