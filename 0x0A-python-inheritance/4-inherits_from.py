#!/usr/bin/python3
''' inherits
'''


def inherits_from(obj, a_class):
    ''' eturns True if the object is an instance
        of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False
    '''
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
