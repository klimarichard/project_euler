import math


def divisors(n):
    """
    Returns number of divisors of given number.
    :param n: an integer
    :return: number of divisors
    """
    divs = [x for x in range(1, round(math.sqrt(n)) + 1) if n % x == 0]
    divs += [n // x for x in divs]
    divs.sort()

    return len(divs)


def first_triangular_with_more_divisors(k):
    """
    Returns first triangular number with more than k divisors.
    :param k: an integer
    :return: first triangular number with more than k divisors.
    """
    current = 0
    n = 1

    while True:
        current += n
        divs_count = divisors(current)

        if divs_count < k:
            n += 1
        else:
            return current


print(first_triangular_with_more_divisors(500))
