from algorithms import gcd


def find_digit_cancelling_fractions():
    """
    Find product of all four digit cancelling fractions less than one in size with two digits
    in the numerator and denominator
    :return: final product of all four digit cancelling fractions
    """
    num = 1
    denom = 1

    for i in range(1, 10):
        for q in range(1, i):
            for p in range(1, q):
                if (p * 10 + i) * q == p * (i * 10 + q):
                    num *= p
                    denom *= q

    return num, denom


p, q = find_digit_cancelling_fractions()
d = gcd(p, q)

print(q // d)
