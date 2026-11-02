#indexing: similar to list, similar to indexing in C

import numpy as np

vector = np.array([1, 4, 32, 4, 12, 9])
matrix = np.array([[1, 3], [7, 5], [2, 5]])

#indexing
print(vector[0], vector[5]) #error if index out of range
print(matrix[0, 1], matrix[2, 0]) #not like list, lst]i][j]

#slicing: array[start:stop:step] stop excluded
print(vector[1:4], vector[:2], vector[::2], vector[::-1])
print(matrix[1, :]) #Select row at index 1, then take every column.
print(matrix[:, 1]) #Take every row, then select column at index 1.
