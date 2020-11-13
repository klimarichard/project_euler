from algorithms import eratosthenes
from itertools import permutations


def find_prime_permutations():
    """
    Find other 4-digit prime permutation than 1487, 4817, 8147.
    :return: list of 4-digit prime permutation
    """
    primes = [n for n in eratosthenes(10000) if n > 1487]

    for p in primes:
        prime_permutations = [n for n in permutate(p) if n in primes and n != p]

        for q in prime_permutations:
            if (q + (q - p)) in prime_permutations:
                return [p, q, 2 * q - p]


def permutate(n):
    """
    Return all digit-wise permutations of given number.
    :param n: an integer
    :return: list of permutations of n
    """
    return list(set([int(''.join(p)) for p in permutations(str(n))]))


print(''.join([str(x) for x in find_prime_permutations()]))
