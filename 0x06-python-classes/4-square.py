#!/usr/bin/python3
"""this is task4"""


class Square:
    """Squere hangler square"""
    def __init__(self, size=0):
        """size is size of elements"""
        self.__size = size

    def area(self):
        """genera area"""
        return self.__size ** 2

    @property
    def size(self):
        """ size property"""
        return self.__size

    @size.setter
    def size(self, s):
        """ size setter"""
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        if s < 0:
            raise ValueError("size must be >= 0")
        self.__size = s
