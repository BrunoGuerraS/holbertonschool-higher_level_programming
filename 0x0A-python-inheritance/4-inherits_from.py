#!/usr/bin/python3
'''eturns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False
'''


def inherits_from(obj, a_class):
    ''' nherits_from use issubclass'''
    if type(obj) is a_class:
        return False
    return  isinstance(obj, a_class)
