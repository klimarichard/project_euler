from algorithms import eratosthenes


def find_coefficients():
    """
    Find coefficients a and b, where |a| < 1000, |b| <= 1000, for which the quadratic
    formula n^2 + an + b produces the maximum number of primes for consecutive values
    of n, starting with n = 0.
    :return: coefficients a and b
    """
    # list of primes for range of max value of quadratic formula, so for n = 79, a = 999, b = 999
    # incredible formula n^2 - 79n + 1601 produces primes for 0 <= n <= 79 --> n = 79 in this max prime
    primes = eratosthenes(79 * 79 + 999 * 79 + 999)
    # list of primes for range of b (starting with 3, b = 2 is not worth examining)
    primes_1000 = eratosthenes(1000)[1:]

    # a = 1, b = 41 is in search space, so we can set initial maximum to 40 and max coefficients to a = 1, b = 41,
    # because n^2 + n + 41 produces 40 consecutive primes from task description
    max_n = 40
    max_coeffs = (1, 41)

    # study of cases:
    #   n - odd/even
    #   a - odd/even
    #   b - odd/even
    #
    #   1) n = 2k + 1, a = 2l + 1, b = 2m + 1, k, l, m from N_0
    #       (2k + 1) * (2k + 1) + (2l + 1) * (2k + 1) + 2m + 1 =
    #     = 4k^2 + 4k + 1 + 4kl + 2l + 2k + 1 + 2m + 1 =
    #     = 4k(k + l + 1) + 2(k + l + m) + 3 ---> odd number
    #
    #   2) n = 2k, a = 2l + 1, b = 2m + 1, k, l, m from N_0
    #       4k^2 + (2l + 1) * 2k + 2m + 1 =
    #     = 4k^2 + 4lk + 2k + 2m + 1 =
    #     = 4k(k + l) + 2(k + m) + 1 ---> odd number
    #
    #   ==> a odd, b odd produces only odd numbers --> good for searching for primes
    #
    #   3) n = 2k + 1, a = 2l, b = 2m + 1, k, l, m from N_0
    #       (2k + 1) * (2k + 1) + 2l * (2k + 1) + 2m + 1 =
    #     = 4k^2 + 4k + 1 + 4kl + 2l + 2m + 1 =
    #     = 4k(k + 1) + 2(2kl + l + m) + 2 ---> even number
    #
    #   ==> a even, b odd produces even numbers, when n is odd --> not good for searching for primes
    #
    #   4) n = 2k + 1, a = 2l + 1, b = 2m, k, l, m from N_0
    #       (2k + 1) * (2k + 1) + (2l + 1) * (2k + 1) + 2m =
    #     = 4k^2 + 4k + 1 + 4kl + 2l + 2k + 1 + 2m =
    #     = 4k(k + l + 1) + 2(k + l + 1) ---> even number
    #
    #   ==> a odd, b even produces even number, when n is odd --> not good for searching for primes
    #
    # CONCLUSION: only a odd, b odd are good combinations for searching for primes

    # b has to be prime, because for n = 0, n^2 + an + b = 0 + 0 + b = b
    for b in primes_1000:
        # consider only such a, that would produce a non-negative number
        # for small n
        for a in range(-b, 1000, 2):
            # b is a prime, therefore we can start with n = 1
            n = 1
            current = 1 + a + b
            while current in primes:
                n += 1
                current = n * n + a * n + b

            if n > max_n:
                max_coeffs = (a, b)
                max_n = n

    return max_coeffs


coeffs = find_coefficients()

print(coeffs[0] * coeffs[1])
