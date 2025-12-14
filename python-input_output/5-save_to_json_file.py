#!/usr/bin/python3
'''
Module that writes JSON representation
into the file
'''


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        f.write(my_obj)
