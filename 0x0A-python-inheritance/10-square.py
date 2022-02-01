#!/usr/bin/python3
''' class BaseGeometry and methods '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''' square class '''
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)
        super().area()
