#!/usr/bin/python3
'''
Module that checks whether that
class is inherited or not
'''


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
