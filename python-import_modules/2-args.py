#!/usr/bin/python3
import sys
index = 1
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        for arg in sys.argv[1:]:
            print("{}: {}".format(index, arg))
            index += 1
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for arg in sys.argv[1:]:
            print("{}: {}".format(index, arg))
            index += 1
