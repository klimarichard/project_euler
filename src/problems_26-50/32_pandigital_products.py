def find_pandigital_sums():
    """
    Find all 1 through 9 pandigital sums.
    :return: list of 1 through 9 pandigital sums
    """
    sums = set()
    digits = set([i for i in range(1, 10)])

    distinct_four_digits = set([1000 * i + 100 * j + 10 * k + l
                                for i in digits for j in digits for k in digits for l in digits
                                if distinct(i, j, k, l)])

    for n in distinct_four_digits:
        unused_digits = digits - set([int(x) for x in str(n)])
        distinct_one_digits = set([i for i in unused_digits])

        for i in distinct_one_digits:
            unused_digits = digits - set([int(x) for x in str(n)]) - set([int(y) for y in str(i)])
            distinct_fours_digits = set([1000 * i + 100 * j + 10 * k + l
                                         for i in unused_digits for j in unused_digits
                                         for k in unused_digits for l in unused_digits
                                         if distinct(i, j, k, l)])

            for j in distinct_fours_digits:
                if i * j == n:
                    sums |= {n}

        unused_digits = digits - set([int(x) for x in str(n)])
        distinct_two_digits = set([10 * i + j for i in unused_digits for j in unused_digits
                                   if distinct(i, j)])

        for i in distinct_two_digits:
            unused_digits = digits - set([int(x) for x in str(n)]) - set([int(y) for y in str(i)])
            distinct_three_digits = set([100 * i + 10 * j + k
                                         for i in unused_digits for j in unused_digits for k in unused_digits
                                         if distinct(i, j, k)])

            for j in distinct_three_digits:
                if i * j == n:
                    sums |= {n}

    sums = list(sums)
    sums.sort()

    return sums


def distinct(*args):
    """
    Finds out, whether all given arguments are distinct digits.
    :param args: digits
    :return: True, if all are pairwise distinct, False otherwise
    """
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            if args[i] == args[j]:
                return False

    return True


print(sum(find_pandigital_sums()))
