import numpy as np


def lattice_paths(m, n):
    """
    Returns number of paths from the top left corner to the bottom right corner of a m × n grid,
    when it is possible to only go down or right.
    :param m: grid height
    :param n: grid width
    :return: number of paths from the top left corner to the bottom right corner of a m × n grid
    """
    grid = np.ones(shape=(m + 1, n + 1), dtype=int)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[m][n]


print(lattice_paths(20, 20))
