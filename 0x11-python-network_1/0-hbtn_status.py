#!/usr/bin/python3
""" fetching https://intranet.hbtn.io/status """
import urllib.request


def fetching(page):
    """ we're fetching url page"""
    with urllib.request.urlopen(page) as response:
        html = response.read()
        print('Body response:')
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode("utf-8"))


if __name__ == '__main__':
    fetching('https://intranet.hbtn.io/status')
