#!/usr/bin/python3
''' task0
    add 2 integer
    a = int
    b = int
'''


def add_integer(a, b=98):
    ''' add 2 integer
        return a + b
    '''
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
