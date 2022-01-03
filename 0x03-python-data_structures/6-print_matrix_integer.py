#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    e = 0
    while i < (len(matrix)):
        while e < (len(matrix[i])):
            print("{:d}".format(matrix[i][e]), end=" ")
            e += 1
        print("")
        e = 0
        i += 1
