#!/usr/bin/python3
'''
Module that serialize and deserialize data
using pickle module
'''


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.attr_dict = {"Name": name, "Age": age, "Is Student": is_student}

    def serialize(self, filename):
        with open(filename, 'wb') as w_file:
            pickle.dump(self.attr_dict, w_file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as data:
                d = pickle.load(data)
            return cls(d["Name"], d["Age"], d["Is Student"])
        except EOFError:
            print('The file is incomplete or corrupted')

    def display(self):
        for key, value in self.attr_dict.items():
            return "{}: {}".format(key, value)
