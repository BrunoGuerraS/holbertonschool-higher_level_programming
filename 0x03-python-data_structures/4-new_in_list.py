#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy = my_list
        return(copy)
    elif idx > (len(my_list) - 1):
        copy = my_list
        return(copy)
    else:
        newcopy = my_list.copy()
        newcopy[idx] = element
        return(newcopy)
