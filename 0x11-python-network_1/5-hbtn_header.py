#!/usr/bin/python3
"""
display values
"""
from sys import argv


def foo():
    import requests
    """displays the value of the variable"""
    url = argv[1]
    value = 'X-Request-Id'
    html = requests.get(url)
    print(html.headers.get(value))


foo()
