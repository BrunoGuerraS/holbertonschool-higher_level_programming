#!/usr/bin/python3
from models.base import Base
''' we create a class reactangle'''


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
        self.__width = value

    @property
    def height(self):
        ''' getter attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter attribute height'''
        self.__height = value

    @property
    def x(self):
        ''' getter attribute x'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' setter attribute x'''
        self.__x = value

    @property
    def y(self):
        ''' getter attribute y'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' setter attribute y'''
        self.__y = value
