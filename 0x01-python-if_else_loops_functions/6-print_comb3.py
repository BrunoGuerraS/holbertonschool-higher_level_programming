#!/usr/bin/python3
dig1 = 0
dig2 = 1
while dig1 <= 8:
    while dig2 <= 9:
        if dig1 != dig2:
            print("{:d}".format(dig1), end='')
            if dig1 != 8:
                print("{:d}, ".format(dig2), end='')
            else:
                print("{:d}".format(dig2)
        dig2 += 1
    dig2 = dig1 + 1
    dig1 += 1
