#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if not isinstance(i, int):
                continue
            else:
                print("{:d}".format(my_list[count]), end="")
            count += 1
        except IndexError:
            raise
            break

    print()
    return count


my_list = []
