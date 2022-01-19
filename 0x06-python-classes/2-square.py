#!/usr/bin/python3
"""this program is the task2

"""


class Square:
    """Square generates a handle for square

    """
    def __init__(self, size=0):
        """size: is a size of elements

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
