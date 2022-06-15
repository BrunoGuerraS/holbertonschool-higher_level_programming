#!/usr/bin/python3
"""
 Python script that takes in a URL and an email
 address, sends a POST request to the passed URL
 with the email as a parameter, and finally
 displays the body of the response.
"""

import requests
from sys import argv


def sendEmail():
    [url, email] = argv[1:]

    s_value = {"email": email}
    response = requests.post(url, data=s_value)
    print(response.text)


if __name__ == "__main__":
    sendEmail()
