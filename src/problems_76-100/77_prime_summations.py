from algorithms import eratosthenes


def find_primes_summations(k):
    """
    Finds the first number, that can be written as a sum of at least two primes
    more than k ways.
    :param k: lower limit for ways
    :return: first number, that can be written more than k ways
    """
    primes = eratosthenes(100)
    n = 2
    flag = True

    while flag:
        # initialize list for dynamic programming
        ways = [0 for _ in range(n + 1)]
        ways[0] = 1

        # compute elements of the list
        for p in primes:
            for j in range(p, n + 1):
                ways[j] += ways[j - p]

        if ways[n] > k:
            flag = False
        else:
            n += 1

    return n


print(find_primes_summations(5000))
