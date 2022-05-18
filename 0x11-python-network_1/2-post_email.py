#!/usr/bin/python3
"""
takes in a URL and an email, sends
a POST request to the passed URL with the
email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
from sys import argv


def senPost():
    """ we create a post handler function"""
    import urllib.request
    import urllib.parse

    [url, email] = argv[1:]
    prm = {"email": email}
    data = urllib.parse.urlencode(prm)
    subdata = data.encode("ascii")
    req = urllib.request.Request(url, subdata)

    with urllib.request.urlopen(req) as response:
        res = response.read().decode("utf-8")
        print(res)


if __name__ == "__main__":
    senPost()
