#!/usr/bin/python3
'''
Module that writes opposite of JSON representation
into the file
'''


import json


def load_from_json_file(filename):
    '''
    Save to json file function
    '''

    with open(filename) as f:
        my_list = json.loads(f.read())
