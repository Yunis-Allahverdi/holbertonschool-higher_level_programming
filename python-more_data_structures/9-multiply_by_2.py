#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for x, y in a_dictionary.items():
        new_dict[x] = int(y) * 2
    return a_dictionary
    return new_dict


a_dictionary = {}
