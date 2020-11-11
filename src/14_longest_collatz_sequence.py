def collatz(n):
    """
    Returns Collatz sequence for given number.
    :param n: an integer
    :return: Collatz sequence for given integer
    """
    seq = [n]

    while seq[-1] != 1:
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)

    return seq


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
