from algorithms import collatz


def longest_collatz(upper, lower=1):
    """
    Returns a number in given range which has a longest Collatz sequence
    :param upper: upper bound of range
    :param lower: optional lower bound of range (default = 1)
    :return: a number with longest Collatz sequence
    """
    maximum = 0
    max_n = 0

    for i in range(lower, upper):
        length = len(collatz(i))
        if length > maximum:
            maximum = length
            max_n = i

    return max_n


print(longest_collatz(1000000))
