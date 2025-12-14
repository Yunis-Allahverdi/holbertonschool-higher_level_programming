#!/usr/bin/python3
'''
Module that reads text file
'''


def read_file(filename=""):
    '''
    Function that reads file
    '''

    with open('UTF8') as f:
        for line in f:
            print(line, end="")
