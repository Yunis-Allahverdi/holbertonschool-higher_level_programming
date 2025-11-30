#!/usr/bin/python3
def remove_char_at(str, n):
    num = len(str)
    first_part = str[:n]
    last_part = str[n+1:num-1]
    total = first_part + last_part
    print(total, end="")
