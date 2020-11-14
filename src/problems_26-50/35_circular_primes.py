from algorithms import eratosthenes


def find_circular_primes(upper):
    """
    Find all circular primes in given range.
    :param upper: upper bound
    :return: list of all circular primes
    """
    circulars = {2}
    primes = eratosthenes(upper)
    non_prime_digits = {0, 2, 4, 6, 8}

    i = 0
    for p in primes:
        current = {p}
        digits = set([int(x) for x in str(p)])

        # if number contains 0, 2, 4, 6 or 8, all its permutations cannot be primes
        if len(digits.intersection(non_prime_digits)) > 0:
            continue

        if p > 20000 * i:
            print(p)
            i += 1

        length = len(str(p))
        flag = True
        j = 0
        next_n = (p % 10) * 10 ** (length - 1) + p // 10
        while flag and j < length - 1:
            if next_n in primes:
                current |= {next_n}
                next_n = (next_n % 10) * 10 ** (length - 1) + next_n // 10
                j += 1
            else:
                flag = False
                break

        if flag:
            circulars |= current

    circulars = sorted(circulars)

    return circulars


print(len(find_circular_primes(1000000)))
