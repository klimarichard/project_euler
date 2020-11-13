from algorithms import eratosthenes


def find_consecutive_prime_sum(n):
    """
    Find all primes that can be written as sums of consecutive primes up to
    given bound.
    :param n: upper bound
    :return: list of all primes that can be written as sums of consecutive primes
    """
    primes = eratosthenes(n)
    max_length = 0
    max_prime = primes[0]
    max_j = len(primes)

    for i in range(len(primes)):
        for j in range(i + max_length, max_j):
            current = sum(primes[i:j])
            if current < n:
                if current in primes:
                    max_length = j - i
                    max_prime = current
            else:
                max_j = j + 1
                break

    return max_prime


print(find_consecutive_prime_sum(1000000))
