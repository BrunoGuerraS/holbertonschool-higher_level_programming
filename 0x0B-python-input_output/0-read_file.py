#!/usr/bin/python3
''' that reads a text file'''


def read_file(filename=""):
    ''' read_file function'''
    with open(filename, 'r+', encoding="UTF-8") as text:
        read_data = text.read()
        print(read_data, end='')
