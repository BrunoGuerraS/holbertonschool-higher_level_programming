#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(listIntegers):
    """finds a peak in a list of unsorted integers"""
    if not listIntegers:
        return None

    length = len(listIntegers)
    half = int(length / 2)

    # Validate Length only 3.
    if half + 1 >= length and half - 1 < 0:
        return listIntegers[half]
    elif half - 1 < 0:
        if listIntegers[half] > listIntegers[half + 1]:
            return listIntegers[half]
        else:
            return listIntegers[half + 1]
    elif half + 1 >= length:
        if listIntegers[half] > listIntegers[half - 1]:
            return listIntegers[half]
        else:
            return listIntegers[half - 1]

    if listIntegers[half - 1] < listIntegers[half]\
       > listIntegers[half + 1]:
        return listIntegers[half]

    if listIntegers[half + 1] > listIntegers[half - 1]:
        return find_peak(listIntegers[half:])

    return find_peak(listIntegers[:half])
