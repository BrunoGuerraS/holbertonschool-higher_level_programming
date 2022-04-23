#!/usr/bin/python3
""" sends a request to the URL and displays the value """
from sys import argv


def gethead():
    import urllib.request
    import urllib.parse
    """ get header information"""
    url = argv[1]
    key = "X-Request-Id"

    with urllib.request.urlopen(url) as response:
        headinf = dict((response.headers._headers).get(key))
        print(headinf)


if __name__ == '__main__':
    gethead()
