#!/usr/bin/python3
"""
taking in a URL, sends a request to the URL
and displays the body of the response utf-u
"""
from encodings import utf_8
from sys import argv


def triggerFunc():
    """func generate takes information in URL"""
    import urllib.request
    import urllib.error

    urlpath = argv[1]

    try:
        with urllib.request.urlopen(urlpath) as response:
            getdata = response.read().decode("utf_8")
            print(getdata)
    except urllib.error.HTTPError as thiserror:
        print("Error code: {}".format(thiserror))


if __name__ == "__main__":
    triggerFunc()
