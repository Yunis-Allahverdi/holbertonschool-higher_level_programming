#!/usr/bin/python3
'''
Module that includes func which returns True
if obj is instance of class
'''


def is_same_class(obj, a_class):
    '''
    Function that checks whether
    obj is instance of a_class or not
    '''

    if obj is None:
        return False

    elif isinstance(obj, a_class) and type(obj) is not bool:
        return True

    return False
