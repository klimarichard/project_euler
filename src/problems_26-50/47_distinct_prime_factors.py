from algorithms import prime_factors


def find_four_consecutive():
    """
    Find four consecutive numbers, that each have four distinct prime factors.
    :return: four consecutive numbers with four distinct prime factors
    """
    # starting at first number with four distinct prime factors
    i = 2 * 3 * 5 * 7

    while True:
        if len(prime_factors(i)) == 4:
            i += 1
            if len(prime_factors(i)) == 4:
                i += 1
                if len(prime_factors(i)) == 4:
                    i += 1
                    if len(prime_factors(i)) == 4:
                        return i - 3, i - 2, i - 1, i

        i += 1


print(find_four_consecutive()[0])
