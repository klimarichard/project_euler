from algorithms import gen_powers


def find_all_powers():
    """
    Find all powers that have the same number of digits, as is their exponent.
    :return: list of all such powers
    """
    powers = []
    flag = True
    i = 1

    while flag:
        flag = False
        gen = gen_powers(i)
        current = next(gen)

        while current // (10 ** (i - 1)) == 0:
            current = next(gen)

        while current // (10 ** i) == 0:
            # only if some number was added in this iteration,
            # we will continue
            flag = True
            powers.append(current)
            current = next(gen)

        i += 1

    return powers


print(len(find_all_powers()))
