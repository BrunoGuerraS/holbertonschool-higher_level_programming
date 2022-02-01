#!/usr/bin/python3
'''writes a string to a text file'''


def write_file(filename="", text=""):
    ''' function write_file'''
    with open(filename, 'w', encoding="UTF-8") as file:
        write_f = file.write(text)
        return write_f