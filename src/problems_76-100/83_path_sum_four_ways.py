import numpy as np


def dijkstra_algorithm(matrix):
    """
    Computes the shortest path from the top left to the bottom right corner
    of the matrix when moving left, right, up and down with Dijkstra's
    algorithm.
    :param matrix: a matrix with values on the path
    :return: length of the shortest path from top left to bottom right
    """
    # initializing value of "infinity" as the sum of all costs in the graph
    infinity = sum([v for row in matrix for v in row])

    # initialize Dijkstra's algorithm
    distance = np.full(shape=(len(matrix), len(matrix[0])),
                       fill_value=infinity,
                       dtype=int)
    distance[0, 0] = matrix[0][0]
    # active vertices
    A = {(i, j) for i in range(distance.shape[0]) for j in range(distance.shape[1])}

    # we stop once we found the shortest path to the bottom right corner
    while (distance.shape[0] - 1, distance.shape[1] - 1) in A:
        # 1) find vertices with minimal distance so far
        min_distance = infinity
        N = set()
        for v in A:
            current = distance[v]

            if current < min_distance:
                N = {v}
                min_distance = current
            elif current == min_distance:
                N |= {v}

        # 2) remove vertices with minimal distance so far from active vertices
        A -= N

        # 3) actualize values for neighbours of v in N
        for v in N:
            if v[0] + 1 < distance.shape[0]:
                distance[v[0] + 1, v[1]] = min(distance[v[0] + 1, v[1]],
                                               distance[v] + matrix[v[0] + 1][v[1]])
            if v[0] - 1 >= 0:
                distance[v[0] - 1, v[1]] = min(distance[v[0] - 1, v[1]],
                                               distance[v] + matrix[v[0] - 1][v[1]])
            if v[1] + 1 < distance.shape[1]:
                distance[v[0], v[1] + 1] = min(distance[v[0], v[1] + 1],
                                               distance[v] + matrix[v[0]][v[1] + 1])
            if v[1] - 1 >= 0:
                distance[v[0], v[1] - 1] = min(distance[v[0], v[1] - 1],
                                               distance[v] + matrix[v[0]][v[1] - 1])

    return distance[-1, -1]


matrix = []

with open('../../res/p083_matrix.txt', 'r') as f:
    line = f.readline()

    while line:
        matrix.append(list(map(int, line.strip().split(','))))
        line = f.readline()

print(dijkstra_algorithm(matrix))
