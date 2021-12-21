#!/usr/bin/python3
i = 97
while i < 123:
    if i == 101 or i == 113:
        i += 1
        continue
    else:
        print("{:s}".format(chr(i)), end='')
        i += 1
