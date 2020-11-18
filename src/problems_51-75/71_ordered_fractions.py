# we are trying to find reduced p/q < 3/7, so
# for each denominator q, we are trying to find
# a numerator p, such that p < 3q/7
#
# we are also dealing with integers, so 7p < 3q means
# 7p <= 3q - 1
#
# since we are searching for a maximal p/q < 3/7, we
# can find the numerator p for each denominator q as
# the lower whole part of (3q - 1)/7


def find_closest_lesser(numerator, denominator, limit):
    """
    Finds the closest lesser reduced fraction than given reduced fraction,
    with denominator lower than the limit.
    :param numerator: a numerator of the threshold
    :param denominator: a denominator of the threshold
    :param limit: upper bound for denominator of the result
    :return: closest lesser reduced fraction
    """
    num = 0
    denom = 1

    for q in range(1, limit + 1):
        p = int(((numerator * q) - 1) / denominator)

        if denom * p > num * q:
            num = p
            denom = q

    return num, denom


print(find_closest_lesser(3, 7, 1000000)[0])
