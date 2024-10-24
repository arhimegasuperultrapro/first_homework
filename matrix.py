import random

# создаем матрицу
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
    for i in matrix:
        for j in range(m):
            i.append(value)

    return matrix

# для красивого вывода
def comfortable(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

matrix = get_matrix(4, 5, 0)


comfortable(matrix)
