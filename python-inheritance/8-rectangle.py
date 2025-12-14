#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''
Module that has a class which inherits
from another file
'''


class Rectangle(BaseGeometry):
    '''
    Class that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator()
