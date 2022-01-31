#!/usr/bin/python3
''' Class Mylist '''


class MyList(list):
    ''' attributes and methods'''
    def print_sorted(self):
        ''' print sort list'''
        print(sorted(self))
