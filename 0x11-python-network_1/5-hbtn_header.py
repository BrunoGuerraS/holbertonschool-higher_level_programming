#!/usr/bin/python3
import requests
from sys import argv
url = argv[1]
value = 'X-Request-Id'
html = requests.get(url)
print(html.headers.get(value))
