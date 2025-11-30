#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        symbol = "{}".format(chr(i))
    else:
        symbol = "{}".format(chr(i - 32))
    print(symbol, end="")
