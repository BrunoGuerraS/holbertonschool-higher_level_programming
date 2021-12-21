#!/usr/bin/python3
i = 0
coma = ","
while i < 100:
    print("{:d}".format(i), end='')
    if i != 99:
        print("{:s}".format(coma), end=' ')
    else:
        print("")
    i += 1
