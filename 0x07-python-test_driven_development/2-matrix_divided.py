#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix=[]
    new_matrixin = []
    counter = 0
    if type(div) not in[int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) >= 2:
        long_first = len(matrix[0])
        for row in matrix:
            if long_first != len(row):
                raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        new_matrix.append(new_matrixin)
        new_matrixin.clear()
        for colum in row:
            if type(colum) not in(int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                new_matrixin.append(round((colum / div), 2))
    return new_matrix
