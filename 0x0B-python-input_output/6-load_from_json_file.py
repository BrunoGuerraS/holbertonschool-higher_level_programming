#!/usr/bin/python3
''' returns the JSON representation of an object '''


import json
""" Import module json for use method dumps
    for serialized
"""


def load_from_json_file(filename):
    """ Function definition"""
    with open(filename, "r") as file:
        return json.loads(file.read())
