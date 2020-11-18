def pythagorean_triplets_sum(n):
    """
    Returns a list of Pythagorean triplets (a, b, c) that satisfy a + b + c = n.
    :param n: desired sum of the triplet
    :return: list of Pythagorean triplets satisfying the condition
    """
    # we can use several general properties of triangles:
    #  - triangle inequality (mainly c < a + b)
    #
    # as well as some properties of primitive Pythagorean triplets:
    #  - exactly one of a, b is odd (we say a is odd, b is even)
    #  - exactly one of a, b is divisible by 3 (for us, a is divisible by 3)
    #  - exactly one of a, b is divisible by 4 (for us, b is divisible by 4)
    #  - c is of the form 4n + 1
    return [(a, b, n - (a + b)) for a in range(3, n + 1, 3) for b in range(4, n + 1 - (a + 1), 4)
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
