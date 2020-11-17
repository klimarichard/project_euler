from itertools import combinations, permutations


def find_magic_5gons(numbers):
    """
    Find all 5-gons containing numbers from the set.
    :param numbers: a set of numbers
    :return: all possible 5-gons
    """
    five_gons = []
    combs = combinations(numbers, 5)

    for c in combs:
        # we want the largest possible outer ring, so we want
        # all small numbers in the inner ring
        if max(c) != 5:
            continue

        # inner ring of the 5-gon, starting at the top
        # and going clockwise
        perms1 = permutations(c)
        for j in perms1:
            ring = []
            for i in range(5):
                ring.append(j[i])

            remaining = numbers - set(ring)
            perms = permutations(remaining)

            for p in perms:
                # outer ring of the 5-gon, starting at the top left
                # and going clockwise
                outer = []
                for i in range(5):
                    outer.append(p[i])

                if validate_ring(ring, outer):
                    five_gons.append(construct_string(ring, outer))

    return five_gons


def validate_ring(ring, outer):
    """
    Checks, if given 5-gon ring is magic, meaning that each line adds
    to the same number.
    :param ring: inner ring of the 5-gon
    :param outer: outer ring of the 5-gon
    :return: True, if 5-gon ring is magic, False, otherwise
    """
    first_sum = outer[0] + ring[0] + ring[1]

    # three middle lines
    for i in range(1, len(ring) - 1):
        if outer[i] + ring[i] + ring[i + 1] != first_sum:
            return False

    # last line
    if outer[len(ring) - 1] + ring[len(ring) - 1] + ring[0] != first_sum:
        return False

    return True


def construct_string(ring, outer):
    """
    Construct unique string for given 5-gon ring.
    :param ring: inner ring of the 5-gon
    :param outer: outer ring of the 5-gon
    :return: string representation of 5-gon ring
    """
    ls = []
    min_index = outer.index(min(outer))

    for i in range(5):
        ls.append(outer[(min_index + i) % 5])
        ls.append(ring[(min_index + i) % 5])
        ls.append(ring[(min_index + (i + 1)) % 5])

    return ''.join([str(x) for x in ls])


numbers = {i for i in range(1, 11)}

print(max(find_magic_5gons(numbers)))
