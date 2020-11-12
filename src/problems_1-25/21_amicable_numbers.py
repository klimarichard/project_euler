from algorithms import divisors, sum_of_proper_divisors


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
