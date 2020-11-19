# we can generate primitive Pythagorean triples and their multiples,
# until we reach the limit
# we will use Euclid's formula for generating the primitive triples:
#  - we have m, n coprimes, where m > n, exactly one of m, n is even, then
#    - a = m^2 - n^2
#    - b = 2mn
#    - c = m^2 + n^2
#    - perimeter p = a + b + c = m^2 - n^2 + 2mn + m^2 + n^2 = 2m(m + n)
#
#  - this means, that p >= 2m(m + 1), so when 2m(m + 1) reaches the limit,
#    we can stop searching
from algorithms import gcd


def find_triples(limit):
    """
    Find Pythagorean triples with perimeters up to given limit.
    :param limit: limit for the perimeter
    :return: a list containing information about how many Pythagorean triples
             were found for each perimeter below the limit
    """
    perimeters = [0 for _ in range(limit + 1)]
    m = 2

    while 2 * m * (m + 1) < limit:
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                p = 2 * m * (m + n)
                i = 1
                # generating non-primitive triples (multiples of this triple)
                while p * i < limit:
                    perimeters[i * (2 * m * (m + n))] += 1
                    i += 1

        m += 1

    return perimeters


perimeters = find_triples(1500000)

print(len([1 for i in perimeters if i == 1]))
