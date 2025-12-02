#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary
    if key in new_dict: 
        del new_dict[key]
    return a_dictionary
    return new_dict


a_dictionary = {}
