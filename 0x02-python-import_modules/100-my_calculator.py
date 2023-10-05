#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <m> <operator> <n>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] in ops:
        m = int(argv[1])
        n = int(argv[3])
        op = ops[argv[2]]
        result = op(num1, num2)
        print('{:d} {:s} {:d} = {:d}'.format(m, argv[2], n, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
