#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    modulo = number % 10
    if modulo > 5:
        str = "and is greater than 5"
        print("Last digit of {:d} is {:d} {:s}".format(number, modulo, str))
    elif modulo == 0:
        str = "and is 0"
        print("Last digit of {:d} is {:d} {:s}".format(number, modulo, str))
    elif 0 < modulo < 6:
        str = "and is less than 6 and not 0"
        print("Last digit of {:d} is {:d} {:s}".format(number, modulo, str))
else:
    change = number * -1
    modulo = change % 10
    chmodulo = modulo * -1
    str = "and is less than 6 and not 0"
    print("Last digit of {:d} is {:d} {:s}".format(number, chmodulo, str))
