#!/usr/bin/python3
'''
Module that checks whether that
class is inherited or not
'''


def is_kind_of_class(obj, a_class):
    '''
    Function that checks obj
    is or not inherited from class
    '''
    if isinstance(obj, a_class):
        return True
    return False
