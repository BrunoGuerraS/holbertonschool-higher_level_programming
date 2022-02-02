#!/usr/bin/python3
''' returns the JSON representation of an object '''


import json
""" Import module json for use method dumps
    for serialized
"""


def to_json_string(my_obj):
    ''' function  to_json_string'''
    return json.dumps(my_obj)
