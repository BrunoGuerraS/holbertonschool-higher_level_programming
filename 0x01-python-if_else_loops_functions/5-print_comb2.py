#!/usr/bin/python3
i = 0
coma = ", "
while i < 100:
    if i != 99:
        print("{:02d}{:s}".format(i, coma), end='')
    else:
        print("{:d}".format(i))
    i += 1
