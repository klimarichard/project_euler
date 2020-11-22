import numpy as np


def minimal_left_right_path(matrix):
    """
    Computes the shortest path from the leftmost column to the rightmost column
    of the matrix when moving only down, up or to the right.
    :param matrix: a matrix with values on the path
    :return: length of the shortest path from top left to bottom right
    """
    matrix = np.array(matrix)

    # for each column, find the row in the previous column
    # which is the cheapest to get here from, so we compute
    # the solution from back to front

    # initialize solution array
    solution = np.empty(shape=matrix.shape[0], dtype=int)
    for i in range(solution.shape[0]):
        solution[i] = matrix[i, solution.shape[0] - 1]

    for i in range(matrix.shape[0] - 2, -1, -1):
        solution[0] += matrix[0, i]

        for j in range(1, matrix.shape[1]):
            solution[j] = min(solution[j - 1] + matrix[j, i], solution[j] + matrix[j, i])

        for j in range(matrix.shape[0] - 2, -1, -1):
            solution[j] = min(solution[j], solution[j + 1] + matrix[j, i])

    return np.min(solution)


matrix = []

with open('../../res/p082_matrix.txt', 'r') as f:
    line = f.readline()

    while line:
        matrix.append(list(map(int, line.strip().split(','))))
        line = f.readline()

print(minimal_left_right_path(matrix))
