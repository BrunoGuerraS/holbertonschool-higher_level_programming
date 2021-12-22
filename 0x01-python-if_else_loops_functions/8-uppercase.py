#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ref = ord(c)
        if 96 < ref < 123:
            upper = chr(ref - 32)
        else:
            upper = c
        print("{:s}".format(upper), end='')
    print("")
    