#!/usr/bin/python3
''' this project is about classes and object '''


class Rectangle:
    ''' class rectangle '''
    def __init__(self, width=0, height=0):
        ''' initializing w and h'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' generation area of rectangle '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' generation perimeter rectangle '''
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))
