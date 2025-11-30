#!/usr/bin/python3
for i in range(97, 123):
    symbol = "{}".format(chr(i))
    if(symbol == 'q' or symbol == 'e'):
        continue;
    print(symbol, end="")
