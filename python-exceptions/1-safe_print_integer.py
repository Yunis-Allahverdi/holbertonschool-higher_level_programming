#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
    except TypeError:
        print("{} is not an integer".format(value))
