def eratosthenes(number):
    """
    Returns a list of all prime numbers from 2 to given number
    :param number: upper boundary for generating prime numbers
    :return: list containing all prime numbers from 2 to given number
    """
    a = set(range(3, number + 1, 2))
    a |= {2}
    p = 3

    while p <= number ** 0.5:
        a -= set(range(p * p, number + 1, 2 * p))
        p += 2

        # it is pointless to examine numbers that aren't primes themselves
        while p not in a:
            p += 2

    a = list(a)
    a.sort()

    return a


def distinct(digits):
    """
    Finds, if all digits in given list are pairwise distinct.
    :param digits: list of digits
    :return: True, if all digits are pairwise distinct, False, otherwise
    """
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i] == digits[j]:
                return False

    return True


def find_pandigital_primes():
    """
    Find all pandigital primes.
    :return: list of n-digit pandigital primes
    """
    # there cannot be a 9-digit pandigital prime, since
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45, so all 9-digit pandigital
    # numbers are divisible by 9
    pandigitals = []
    primes = eratosthenes(87654321)

    for p in primes:
        digits = [int(x) for x in str(p)]

        if distinct(digits):
            pandigital = True

            # checking, if the numbers are in range (1, 2, ..., n)
            for i in range(1, len(digits) + 1):
                if i not in digits:
                    pandigital = False
                    break

            if pandigital:
                pandigitals.append(p)

    return pandigitals


print(max(find_pandigital_primes()))
