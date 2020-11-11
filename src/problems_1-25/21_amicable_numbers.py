import math


def divisors(n):
    """
    Returns divisors of given number.
    :param n: an integer
    :return: list of divisors
    """
    divs = [x for x in range(1, round(math.sqrt(n)) + 1) if n % x == 0]
    divs += [n // x for x in divs]
    divs = list(set(divs))
    divs.sort()

    return divs


def sum_of_proper_divisors(divisors):
    """
    Returns sum of proper divisors.
    :param divisors: list of all divisors
    :return: sum of proper divisors
    """
    return sum(divisors[:-1])


def find_amicables_sum(upper, lower=1):
    """
    Returns sum af amicable numbers in given range.
    :param upper: upper bound
    :param lower: optional lower bound (default = 1)
    :return: sum of amicable numbers in give range
    """
    sum = 0

    for a in range(lower, upper):
        b = sum_of_proper_divisors(divisors(a))
        if a != b and sum_of_proper_divisors(divisors(b)) == a:
            sum += a + b

    # each pair was counted twice, so we return half of the sum
    return sum // 2


print(find_amicables_sum(10000))
