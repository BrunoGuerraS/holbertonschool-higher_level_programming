#!/usr/bin/python3
''' class BaseGeometry and methods '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''' square class '''
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)

