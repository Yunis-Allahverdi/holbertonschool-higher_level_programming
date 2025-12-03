#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            if not isinstance(my_list[i], int):
                continue
            else:
                print("{:d}".format(my_list[i]), end="")
                a += 1
        except IndexError:
            raise
            break

    print()
    return a


my_list = []
