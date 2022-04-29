#!/usr/bin/python3
import requests
from sys import argv

path = argv[1]
value = 'X-Request-Id'
html = requests.get(path)
print(html.headers.get(value))
