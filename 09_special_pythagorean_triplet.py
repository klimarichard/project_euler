def pythagorean_triplets_sum(n):
    """
    Returns a list of Pythagorean triplets (a, b, c) that satisfy a + b + c = n.
    :param n: desired sum of the triplet
    :return: list of Pythagorean triplets satisfying the condition
    """
    return [(a, b, c) for a in range(1001) for b in range(a, 1001) for c in range(1, a + b)
            if a * a + b * b == c * c and a + b + c == 1000]


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
