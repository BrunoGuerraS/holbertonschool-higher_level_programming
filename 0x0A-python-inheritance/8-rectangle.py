#!/usr/bin/python3
''' class BaseGeometry and methods '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' take a base geometry and add width and height'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
