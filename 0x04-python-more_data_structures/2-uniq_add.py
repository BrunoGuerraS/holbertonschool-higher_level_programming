#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(list(map(lambda i: i, list(set(my_list)))))
