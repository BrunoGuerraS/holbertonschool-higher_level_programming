#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="UTF-8") as text:
        read_data = text.read()
        print(read_data)
