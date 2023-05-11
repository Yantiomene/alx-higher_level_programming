#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    nargs = len(argv)
    if nargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == '+':
        print("{:d} {} {:d} = {}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{:d} {} {:d} = {}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{:d} {} {:d} = {}".format(a, op, b, mul(a, b)))
    elif op == '/':
        print("{:d} {} {:d} = {}".format(a, op, b, div(a, b)))
