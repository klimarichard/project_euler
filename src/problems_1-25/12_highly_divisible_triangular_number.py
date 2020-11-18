from algorithms import divisors


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

        if len(divs_count) < k:
            n += 1
        else:
            return current


print(first_triangular_with_more_divisors(500))
