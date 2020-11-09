def square_of_sum(n):
    """
    Returns squared sum of first n numbers.
    :param n: an integer
    :return: squared sum of first n numbers
    """
    return ((n * (n + 1)) // 2) * ((n * (n + 1)) // 2)


def sum_of_squares(n):
    """
    Returns sum of squares of first n numbers.
    :param n: an integer
    :return: sum of squares of first n numbers
    """
    return sum([i * i for i in range(1, n + 1)])


sq_sm = square_of_sum(100)
sm_sq = sum_of_squares(100)

print(sq_sm - sm_sq)
