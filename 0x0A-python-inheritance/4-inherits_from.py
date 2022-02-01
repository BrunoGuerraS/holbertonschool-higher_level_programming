#!/usr/bin/python3
'''eturns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False
'''


def inherits_from(obj, a_class):
    ''' nherits_from use issubclass'''
    return not issubclass(a_class, type(obj))
