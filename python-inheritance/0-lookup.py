#!/usr/bin/python3
'''
This module used for write a function
that returns available attributes of an object
'''


def lookup(obj):
    '''
    Function that returns all the attributes of any given object
    '''
    return dir(obj)
