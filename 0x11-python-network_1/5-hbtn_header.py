#!/usr/bin/python3
"""
display values
"""
import requests
from sys import argv


def foo():
    """displays the value of the variable"""
    url = argv[1]
    value = 'X-Request-Id'
    html = requests.get(url)
    print(html.headers.get(value))


foo()
