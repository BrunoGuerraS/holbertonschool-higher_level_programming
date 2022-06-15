#!/usr/bin/python3
"""
script that takes in a URL, sends a request
to the URL and displays the body of the response
"""


import requests
from sys import argv


def showbody():
    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    showbody()
