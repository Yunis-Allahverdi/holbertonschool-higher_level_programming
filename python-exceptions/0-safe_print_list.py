#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 1
    for i in my_list:
        index += 1

    try:
        if x > index:
            raise IndexError("Try again")
        else:
            for i in range(x):
                print(my_list[i], end="")

            np_print = int(x)
            print("{:d}".format(np_print))
    except IndexError as i:
        print(i)


my_list = []
