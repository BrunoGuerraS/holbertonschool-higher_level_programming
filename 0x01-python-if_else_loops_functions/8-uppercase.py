#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ref = ord(c)
        if 96 < ref < 123:
            print("{:s}".format(chr(ref - 32)), end='')
        else:
            print("{:s}".format(c), end='')
    print("")
