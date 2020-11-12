from algorithms import is_hexagonal, is_pentagonal


def find_next(i):
    """
    Find next triangular number after given index which is also pentagonal
    and hexagonal.
    :param i: starting index
    :return: next triangular number which is also pentagonal and hexagonal
    """
    i += i

    while True:
        current = i * (i + 1) // 2
        if is_pentagonal(current) and is_hexagonal(current):
            return current
        else:
            i += 1


print(find_next(285))
