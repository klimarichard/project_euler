def find_all_coin_sums(n):
    """
    Counts how many ways can a given amount of money be made using any number of coins.
    :param n: target amount of money
    :return: number of way to obtain £n
    """
    # initialize list for dynamic programming
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1

    # compute elements of the list
    for x in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(x, n + 1):
            ways[i] += ways[i - x]

    return ways[-1]


print(find_all_coin_sums(200))
