#!/usr/bin/python3
'''
Empty Module
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Inherited Class
    '''

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)
