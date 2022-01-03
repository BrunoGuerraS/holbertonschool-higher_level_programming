#!/usr/bin/env python3
def no_c(my_string):
    newString = []
    for i in my_string:
        if (i == 'c') or (i == 'C'):
            continue
        else:
            newString.append(i)
    sinc = ""
    sinc = sinc.join(newString)
    return(sinc)
