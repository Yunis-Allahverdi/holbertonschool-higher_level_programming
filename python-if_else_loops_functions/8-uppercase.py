#!/usr/bin/python3
index = 0


def uppercase(str):
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            letter = ord(i) - 32
            symbol = "{}".format(chr(letter))
        else:
            symbol = "{}".format(i)
        if index == len(str) - 1:
            print(symbol)
        else:
            print(symbol, end="")
            index += 1
