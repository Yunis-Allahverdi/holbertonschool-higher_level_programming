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
        with open(filename, 'rb') as r_file:
            print(pickle.load(r_file))

        obj = cls(data["Name"], data["Age"], data["Is Student"])


    def display(self):
        for key, value in self.attr_dict.items():
            return "{}: {}".format(key, value)
