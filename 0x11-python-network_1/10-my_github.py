#!/usr/bin/python3
"""
 script that takes your GitHub credentials
"""


import requests
from sys import argv


def getgithub():
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(argv[1], argv[2]))
    response = response.json()
    print(response.get("id"))


if __name__ == "__main__":
    getgithub()
