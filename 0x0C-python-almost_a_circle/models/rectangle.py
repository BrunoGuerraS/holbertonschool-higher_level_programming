#!/usr/bin/python3
''' we create a class reactangle'''
from models.base import Base


class Rectangle(Base):
    ''' class rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor method'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' getter attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter attribute width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' getter attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' getter attribute x'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' setter attribute x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' getter attribute y'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' setter attribute y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width
