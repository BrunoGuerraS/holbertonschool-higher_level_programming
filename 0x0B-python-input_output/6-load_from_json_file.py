#!/usr/bin/python3
''' returns the JSON representation of an object '''


import json
""" Import module json for use method dumps
    for serialized
"""


def save_to_json_file(my_obj, filename):
    ''' save_to_json_file function '''
    with open(filename, 'r') as file:
        return json.loads(file)
