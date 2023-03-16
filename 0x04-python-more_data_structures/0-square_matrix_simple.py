#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrixes = []
    for i in matrix:
        row_matrix = []
        for j in i:
            row_matrix.append(j ** 2)
        matrixes.append(row_matrix)
    return matrixes
