#!/usr/bin/python3
def safe_print_integer(value):
    try:
        a = int(value)
        print("{:d}".format(a))
        return(True)
    except:
        return (False)
