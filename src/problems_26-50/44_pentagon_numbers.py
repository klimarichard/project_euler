from algorithms import is_pentagonal


def find_minimal_pair():
    """
    Find minimal pair of pentagonal numbers
    :return:
    """
    i = 1

    while True:
        for j in range(1, i):
            p1 = i * (3 * i - 1) // 2
            p2 = j * (3 * j - 1) // 2

            if is_pentagonal(p1 + p2) and is_pentagonal(p1 - p2):
                return p1 - p2

        i += 1


print(find_minimal_pair())
