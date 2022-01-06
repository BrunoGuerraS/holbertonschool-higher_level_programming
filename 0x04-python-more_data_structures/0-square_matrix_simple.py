#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for o in matrix[i]:
            new_matrix[i].append(o ** 2)
    return new_matrix
