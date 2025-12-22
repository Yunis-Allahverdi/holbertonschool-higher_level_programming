#!/usr/bin/python3

from calculator_1.py import add, sub, div, mul
from sys import argv

if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[2] == '+':
            print("{} {} {} = {} ".format(sys.argv[1], sys.argv[2], sys.argv[3], add(sys.argv[1],sys.argv[3])))
        elif sys.argv[2] == '-':
            print("{} {} {} = {} ".format(sys.argv[1], sys.argv[2], sys.argv[3], sub(sys.argv[1],sys.argv[3])))
        elif sys.argv[2] == '*':
            print("{} {} {} = {} ".format(sys.argv[1], sys.argv[2], sys.argv[3], mul(sys.argv[1],sys.argv[3])))
        elif sys.argv[2] == '/':
            print("{} {} {} = {} ".format(sys.argv[1], sys.argv[2], sys.argv[3], div(sys.argv[1],sys.argv[3])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            return 1
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
