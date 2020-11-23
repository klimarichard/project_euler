from algorithms import eratosthenes


def prime_power_triples(n):
    """
    Find all numbers in given range, that can be written as a sum of a squared prime,
    a cubed prime and a prime to the power of four.
    :param n: upper limit
    :return: list of numbers that can be written in such way
    """
    primes = eratosthenes(int(n ** 0.5) + 1)
    squares = [p ** 2 for p in primes if p ** 2 < n]
    cubes = [p ** 3 for p in primes if p ** 3 < n]
    fourths = [p ** 4 for p in primes if p ** 4 < n]

    satisfying = set()

    for s in squares:
        for c in cubes:
            for f in fourths:
                if s + c + f > n:
                    break

                satisfying |= {s + c + f}

    return sorted(set(satisfying))


print(len(prime_power_triples(50000000)))
