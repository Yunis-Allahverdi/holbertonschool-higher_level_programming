#!/usr/bin/python3
'''
This module provides function and class
for editing lists
'''


class MyList(list):
    '''
    A class that inherits from list
    '''

    def print_sorted(self):
        print self.sort()

    def append(self, item):
        super().append(item)
