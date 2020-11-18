def pythagorean_triplets_sum(n):
    """
    Returns a list of Pythagorean triplets (a, b, c) that satisfy a + b + c = n.
    :param n: desired sum of the triplet
    :return: list of Pythagorean triplets satisfying the condition
    """
    # we can use several general properties of triangles:
    #  - triangle inequality (mainly c < a + b)
    #
    # and some properties for Pythagorean triangles:
    #  - a < b < c, so a < n/3 and a < b < n/2
    return [(a, b, n - (a + b)) for a in range(1, int(n / 3) + 1) for b in range(a, int(n / 2) + 1)
            if (a % 2 != b % 2) and a * a + b * b == ((n - (a + b)) * (n - (a + b)))]


def triplet_products(triplets):
    """
    Returns list of products of triplets from given list of triplets.
    :param triplets: list of triplets
    :return: list of products of triplets from given list
    """
    if len(triplets) == 0:
        return None
    else:
        return [a * b * c for (a, b, c) in triplets]


print(triplet_products(pythagorean_triplets_sum(1000))[0])
