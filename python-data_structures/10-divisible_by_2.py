#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for i in my_list:
        if i % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return list_result


list_result = divisible_by_2(my_list)
i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
