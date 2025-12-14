#!/usr/bin/python3
'''
Module that checks whether that
class is inherited or not
'''


def inherits_from(obj, a_class):
    '''
    Function that checks obj
    is or not inherited from class
    (directly or undirectly)
    '''

    if isinstance(obj, a_class):
        return True
    return False
