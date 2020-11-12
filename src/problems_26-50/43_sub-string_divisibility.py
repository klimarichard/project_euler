from itertools import permutations


def sub_string_divisible(pandigitals):
    """
    Finds all pandigital numbers with sub-string divisibility property.
    :param pandigitals: list of all pandigital numbers
    :return: list of sub-string divisible pandigital numbers
    """
    divisible = []

    for p in pandigitals:
        if (int(''.join(p[1:4])) % 2 == 0 and
                int(''.join(p[2:5])) % 3 == 0 and
                int(''.join(p[3:6])) % 5 == 0 and
                int(''.join(p[4:7])) % 7 == 0 and
                int(''.join(p[5:8])) % 11 == 0 and
                int(''.join(p[6:9])) % 13 == 0 and
                int(''.join(p[7:10])) % 17 == 0):
            divisible.append(int(''.join(p)))

    return divisible


print(sum(sub_string_divisible(permutations('0123456789'))))
