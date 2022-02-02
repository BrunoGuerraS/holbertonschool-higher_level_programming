#!/usr/bin/python3
''' appends a string at the end of a text file '''


def append_write(filename="", text=""):
    ''' function append_write'''
    with open(filename, 'a', encoding="UTF-8") as file:
        append_f = file.write(text)
        return append_f
