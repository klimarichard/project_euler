from algorithms import eratosthenes


def find_truncatable_primes():
    """
    Find all primes truncatable from left to right and right to left.
    :return: list of all truncatable primes
    """
    truncatable = []

    # upper bound is arbitrary, but I couldn't find in analytically
    primes = eratosthenes(1000000)
    non_prime_digits = {0, 2, 4, 6, 8}

    # we can consider only primes greater than 20, since one digit primes are not
    # considered truncatable, and primes starting with one cannot be truncatable,
    # since 1 is not a prime
    for p in list(filter(lambda x: x > 20, primes)):
        length = len(str(p))

        digits = set([int(x) for x in str(p)])

        # if number contains 0, 2, 4, 6 or 8, all its permutations cannot be primes
        if len(digits.intersection(non_prime_digits)) > 0:
            if p // (10 ** (length - 1)) != 2:
                continue

        # if the number has a leading 1 or ends with 1, it cannot be truncatable,
        # since 1 is not a prime
        if p % 10 == 1 or p // (10 ** (length - 1)) == 1:
            continue

        flag = True
        for k in range(1, length):
            trunc_r = (p - (p % (10 ** k))) // (10 ** k)
            trunc_l = p - (p // (10 ** (length - k))) * (10 ** (length - k))

            if trunc_r in primes and trunc_l in primes:
                continue
            else:
                flag = False
                break

        if flag:
            truncatable.append(p)

    return truncatable


print(sum(find_truncatable_primes()))
