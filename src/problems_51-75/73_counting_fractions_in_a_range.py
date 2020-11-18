# for each denominator q, the first numerator p to be considered
# is the upper whole part of q/3, and the last p to be considered
# is the lower whole part of q/2


from algorithms import gcd


def find_all_between(numerator_low, denominator_low, numerator_high,
                     denominator_high, limit):
    """
    Finds all reduced fraction between given two fractions, for which
    the denominator is at most the limit.
    :param numerator_low: numerator of the lower bound
    :param denominator_low: denominator of the lower bound
    :param numerator_high: numerator of the upper bound
    :param denominator_high: denominator of the upper bound
    :param limit: a limit for the denominator
    :return: list of reduced fractions in given range
    """
    fractions = []

    for q in range(1, limit + 1):
        p_low = int((numerator_low * q) / denominator_low) + 1
        p_high = int(((numerator_high * q) - 1) / denominator_high)

        for p in range(p_low, p_high + 1):
            if gcd(p, q) == 1:
                fractions.append((p, q))

    return fractions


print(len(find_all_between(1, 3, 1, 2, 12000)))
