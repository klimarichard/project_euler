from algorithms import eratosthenes


def find_minimal_permuted_totient(n):
    """
    Find a number in the given range, which is a permutation of
    the value of its totient function and produces the minimal ratio n/φ(n).
    :param n: upper bound
    :return: a number with minimal n/φ(n) where φ(n) is a permutation of n
    """
    # we need a list of primes around sqrt(n), because there is
    # a high chance for pairs of such primes to produce desired result
    primes = eratosthenes(int((n ** 0.5) * 1.3))
    del primes[:int(0.6 * len(primes))]

    min_ratio = n + 1
    min_n = 1
    i = 0

    for p in primes:
        i += 1
        for q in primes[i:]:
            k = p * q

            if k > n:
                return min_n

            phi = (p - 1) * (q - 1)

            if not is_permutation(k, phi):
                continue

            if k / phi < min_ratio:
                min_ratio = k / phi
                min_n = k

    return min_n


def is_permutation(m, n):
    """
    Finds, if one number is a permutation of the other.
    :param m: first integer
    :param n: second integer
    :return: True, if the two numbers are permutations of each other,
             False, otherwise
    """
    if len(str(m)) != len(str(n)):
        return False

    m_list = [int(x) for x in str(m)]
    n_list = [int(x) for x in str(n)]

    for x in m_list:
        if x in n_list:
            n_list.remove(x)
        else:
            return False

    return True


print(find_minimal_permuted_totient(10 ** 7))
