def find_digit_cancelling_fractions():
    """
    Find product of all four digit cancelling fractions less than one in size with two digits
    in the numerator and denominator
    :return: final product of all four digit cancelling fractions
    """
    dcf = []
    num = 1
    denom = 1

    for i in range(1, 10):
        for q in range(1, i):
            for p in range(1, q):
                if (p * 10 + i) * q == p * (i * 10 + q):
                    num *= p
                    denom *= q

    return num, denom


def gcd(a, b):
    """
    Computes greatest common divisor using the basic Euclidean algorithm.
    :param a: first integer
    :param b: second integer
    :return: GCD(a, b)
    """
    if b > a:
        temp = a
        a = b
        b = temp

    if b == 0:
        return a
    else:
        return gcd(a % b, b)


p, q = find_digit_cancelling_fractions()
d = gcd(p, q)

print(q // d)
