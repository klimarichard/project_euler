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


def find_abundant(upper, lower=1):
    """
    Find all abundant numbers in given range.
    :param upper: upper bound
    :param lower: optional lower bound (default = 1)
    :return: list of abundant numbers in given range
    """
    abundants = []

    for i in range(lower, upper):
        if sum_of_proper_divisors(divisors(i)) > i:
            abundants.append(i)

    return abundants


def find_non_writtable(upper, lower=1):
    """
    Find all numbers in given range that cannot be written as a sum of two abundant numbers.
    :param upper: upper bound
    :param lower: optional lower bound (default = 1)
    :return: list of numbers that cannot be written as a sum of two abundant numbers
    """
    abundants = find_abundant(upper)
    n = lower

    writtables = set([x + y for x in abundants for y in abundants if x + y < upper])

    non_writtables = set(range(28123)) - writtables

    return list(non_writtables)


print(sum(find_non_writtable(28123)))
