#!/usr/bin/python3
'''
Module that does both serialization
and deserialization
'''


import json


def serialize_and_save_to_file(data, filename):
    '''
    Function that serializes data
    and save to json file
    '''
    with open(filename, 'w', encoding='utf-8') as write_json:
        json.dump(data, write_json, indent=4)


def load_and_deserialize(filename):
    '''
    Function that deserializes data
    from json file
    '''
    with open(filename, 'r', encoding='utf-8') as read_json:
        return json.load(data, read_json)
