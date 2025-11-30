#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            letter = ord(i) - 32
            symbol = "{}".format(chr(letter))
        else:
            symbol = "{}".format(i)
        if i == len(str) - 1:
            print(symbol, end="\n")
        else:
            print(symbol, end="")
