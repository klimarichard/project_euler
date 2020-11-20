from algorithms import eratosthenes


def find_primes_summations(n):
    """
    Finds how many ways can numbers up to given integer be written as a sum of
    at least two primes.
    :param n: an integer
    :return: number of ways to write numbers 1 to n as a summation of primes
    """
    primes = eratosthenes(n)

    # initialize list for dynamic programming
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1

    # compute elements of the list
    for p in primes:
        for j in range(p, n + 1):
            ways[j] += ways[j - p]

    return ways


# 100 was chosen arbitrarily, but I couldn't find it analytically
prime_sums = find_primes_summations(100)

print(prime_sums.index(list(filter(lambda x: x > 5000, prime_sums))[0]))
