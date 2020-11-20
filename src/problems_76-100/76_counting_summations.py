def find_summations(n):
    """
    Finds how many ways can given integer be written as a sum of
    at least two positive integers.
    :param n: an integer
    :return: number of ways to write n as a summation
    """
    # initialize list for dynamic programming
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1

    # compute elements of the list
    for i in range(1, n):
        for j in range(i, n + 1):
            ways[j] += ways[j - i]

    return ways[-1]


print(find_summations(100))
