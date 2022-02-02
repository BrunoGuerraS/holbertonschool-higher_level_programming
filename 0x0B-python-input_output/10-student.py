#!/usr/bin/python3
''' defines a student by: based on 9-student.py'''


class Student:
    ''' class student '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for key in self.__dict__.keys():
            if key in attrs:
                my_dict[key] = self.__dict__[key]
        return my_dict
