#!/usr/bin/python3
for a in range(10):
    for b in range(a+1, 10):
        digits = "{}{}".format(a, b)
        if digits == "89":
            print(digits, end="\n")
        else:
            print(digits, end=", ")
