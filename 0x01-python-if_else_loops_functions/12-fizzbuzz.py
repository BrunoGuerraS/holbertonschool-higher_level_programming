#!/usr/bin/python3
def fizzbuzz():
    i = 1
    for i in range(101):
        if i == 100:
            print("{:s} ".format("Buzz"), end='')
        elif i % 3 == 0 or i % 5 == 0 or i % 3 == 0 and i % 5 == 0:
            if i % 3 == 0 and i % 5 == 0:
                print("{:s} ".format("FizzBuzz"), end='')
            elif i % 3 == 0:
                print("{:s} ".format("Fizz"), end='')
            elif i % 5 == 0:
                print("{:s} ".format("Buzz"), end='')
        else:
            print("{:d} ".format(i), end='')