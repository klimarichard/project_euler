from algorithms import prime_factors_list


def find_totient_ratio(n, kind='max'):
    """
    Find a number n in given range for which the ratio n/φ(n) is maximal.
    :param n: upper bound
    :param kind: optional parameter (default = 'max') determining, whether
                 a maximum or minimum ratio should be returned
    :return: a number with maximal ratio
    """
    # by definition of Euler's phi function, it holds:
    # φ(n) = p_1^(k_1 - 1) * (p_1 - 1) * p_2^(k_2 - 1) * (p_2 - 1) * ... *
    #        * p_r^(k_r - 1) * (p_r - 1), for
    # n = p_1^(k_1) * p_2^(k_2) * ... * p_r^(k_r), where
    # p_1, p_2, ..., p_r are distinct primes, that divide n
    if kind == 'max':
        max_ratio = 1
        max_n = 1
    elif kind == 'min':
        min_ratio = n + 1
        min_n = 1
    else:
        return None

    for k in range(2, n + 1):
        phi = totient(k)

        if kind == 'max':
            if k / phi > max_ratio:
                max_ratio = k / phi
                max_n = k
        if kind == 'min':
            if k / phi < min_ratio:
                min_ratio = k / phi
                min_n = k

    if kind == 'max':
        return max_n
    else:
        return min_n


def totient(n):
    """
    Computes value of totient function of given number.
    :param n: an integer
    :return: value of the totient function
    """
    phi = 1
    divs = prime_factors_list(n)

    for p in range(len(divs)):
        phi *= ((divs[p][0] ** (divs[p][1] - 1)) * (divs[p][0] - 1))

    return phi


print(find_totient_ratio(1000000))
