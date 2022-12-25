import numpy as np

def transpose_matrix(m):
    transposed = m.transpose()
    return transposed

matrix1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


matrix2 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,0]
])

matrix3 = np.array([
    [5,6,7,8]
])

print(transpose_matrix(matrix))