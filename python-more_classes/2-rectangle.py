#!/usr/bin/python3
'''
This module created for defining rectangle
based on private height and width attribute
'''


class Rectangle:
    '''
    This class used for defining the size of rectangle
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        else:
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not type(height) is int:
            raise TypeError("height must be an integer")
        else:
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0

        return (self.height + self.width) * 2


r1 = Rectangle(20, 30)
