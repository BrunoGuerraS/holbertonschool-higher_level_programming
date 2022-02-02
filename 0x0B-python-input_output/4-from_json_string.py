#!/usr/bin/python3
''' returns the JSON representation of an object '''


import json
""" Import module json for use method dumps
    for serialized
"""


def from_json_string(my_str):
    ''' function from_json_string '''
    return json.loads(my_str)
