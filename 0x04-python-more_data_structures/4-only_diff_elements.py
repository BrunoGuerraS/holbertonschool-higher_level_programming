#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    l1 = list(set_1)
    l2 = list(set_2)
    l3 = l1 + l2
    i = 0
    while i < len(l3):
        value = l3.count(l3[i])
        if value > 1:
            vr = l3[i]
            for a in range(value):
                l3.remove(vr)
            i = 0
        i += 1
    l4 = {x for x in l3}
    return l4
