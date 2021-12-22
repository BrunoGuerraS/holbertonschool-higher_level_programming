#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        posnomb = number * -1
        last = posnomb % 10
    else:
        last = number % 10
    print("{:d}".format(last), end='')
    return last
