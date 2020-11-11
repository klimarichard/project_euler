def find_distinct_powers(a, b):
    """
    Find all distinct powers of numbers a^b.
    :param a: upper bound for a
    :param b: upper bound for b
    :return: list of distinct powers of a^b
    """
    distinct = set()

    for x in range(2, a + 1):
        for y in range(2, b + 1):
            current = x ** y
            if current not in distinct:
                distinct |= {current}

    distinct = list(distinct)
    distinct.sort()

    return distinct


print(len(find_distinct_powers(100, 100)))
