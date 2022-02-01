#!/usr/bin/python3
''' class BaseGeometry and methods '''


class BaseGeometry:
    ''' there are no methods '''

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

    def area(self):
        raise Exception("area() is not implemented")
