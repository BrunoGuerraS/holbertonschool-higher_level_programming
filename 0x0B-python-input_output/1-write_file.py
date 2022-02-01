#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF-8") as file:
        write_f = file.write(text)
        return write_f