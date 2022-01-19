#!/usr/bin/python3
"""This program is the task3

"""


class Square:
    """Squere hangler square

    """
    def __init__(self, size=0):
        """size is size of elements

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """genera area

        """
        return self.__size ** 2
