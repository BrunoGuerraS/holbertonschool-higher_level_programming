#!/usr/bin/python3
"""
taking in a URL, sends a request to the URL
and displays the body of the response utf-u
"""


def triggerFunc():
    """func generate takes information in URL"""
    import urllib.request
    import urllib.error
    from sys import argv
    urlpath = argv[1]

    try:
        with urllib.request.urlopen(urlpath) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as thiserror:
        print('Error code: {}'.format(thiserror.code))


if __name__ == "__main__":
    triggerFunc()
