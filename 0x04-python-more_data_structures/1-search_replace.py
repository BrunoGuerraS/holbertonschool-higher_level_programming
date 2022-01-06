#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if my_list == 0 or my_list is None:
        return None
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
