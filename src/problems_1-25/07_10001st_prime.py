def find_nth_prime(n):
    """
    Finds n-th prime number.
    :param n: an integer
    :return: n-th prime number
    """
    primes = [2]
    candidate = 3

    while len(primes) < n:
        # if next number is not divisible by any other prime, it is itself a prime
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)

        # no need to check even numbers, the only even prime is 2
        candidate += 2

    return primes[-1]


print(find_nth_prime(10001))
