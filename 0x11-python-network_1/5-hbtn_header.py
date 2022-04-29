#!/usr/bin/python3
"""
Displays the value of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    path = argv[1]
    res = requests.get(path)
    print(res.headers.get("X-Request-Id"))
