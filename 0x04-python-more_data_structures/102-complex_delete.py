#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    s = a_dictionary.copy()
    for key in s.keys():
        if a_dictionary.get(key) == value:
            a_dictionary.pop(key)
    return a_dictionary
