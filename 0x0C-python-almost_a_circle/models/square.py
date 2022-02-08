#!/usr/bin/python3
''' class Square '''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''this class give us a square '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' the size '''
        return self.width

    @size.setter
    def size(self, value):
        ''' getter size'''
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string with rectangle to stdout"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
    
    def update(self, *args, **kwargs):
        ''' assings attributes'''
        keys = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])
