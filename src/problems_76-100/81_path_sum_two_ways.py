import numpy as np


def minimal_top_bottom_path(matrix):
    """
    Computes the shortest path from the top left to the bottom right corner
    of the matrix when moving only down or to the right with Dijkstra's
    algorithm.
    :param matrix: a matrix with values on the path
    :return: length of the shortest path from top left to bottom right
    """
    matrix = np.array(matrix)

    # for each column, find the row in the previous column
    # which is the cheapest to get here from, so we compute
    # the solution from back to front
    for i in range(matrix.shape[1] - 2, -1, -1):
        matrix[matrix.shape[1] - 1, i] += matrix[matrix.shape[1] - 1, i + 1]
        matrix[i, matrix.shape[1] - 1] += matrix[i + 1, matrix.shape[1] - 1]

    for i in range(matrix.shape[1] -2, -1, -1):
        for j in range(matrix.shape[1] - 2, -1, -1):
            matrix[i, j] += min(matrix[i + 1, j], matrix[i, j + 1])

    return matrix[0, 0]


matrix = []

with open('../../res/p081_matrix.txt', 'r') as f:
    line = f.readline()

    while line:
        matrix.append(list(map(int, line.strip().split(','))))
        line = f.readline()

print(minimal_top_bottom_path(matrix))
