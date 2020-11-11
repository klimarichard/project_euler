def find_recurring_sequence(p, q):
    """
    Finds recurring sequence in a decimal representation of a fraction.
    :param p: numerator
    :param q: denominator
    :return: recurring sequence of a decimal fraction
    """
    current_mod = p % q
    current_div = p // q

    mods = []
    divs = []

    while current_mod != 0 and current_mod not in mods:
        mods.append(current_mod)
        divs.append(current_div)

        p = current_mod * 10
        current_mod = p % q
        current_div = p // q

    if current_mod == 0:
        return []
    else:
        divs.append(current_div)
        return divs[mods.index(current_mod) + 1:]


def find_max_recurring_sequence(upper, lower=1):
    """
    Finds the denominator with the longest recurring sequence between bounds.
    :param upper: upper bound for denominator
    :param lower: optional lower bound for denominator (default = 1)
    :return: denominator with longest recurring sequence
    """
    max_seq = 0
    max_int = lower
    for i in range(lower, upper):
        current = len(find_recurring_sequence(1, i))
        if current > max_seq:
            max_seq = current
            max_int = i

    return max_int


print(find_max_recurring_sequence(1000))
