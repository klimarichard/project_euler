def generate_four_digit_numbers():
    """
    Generates all triangle, square, pentagonal, hexagonal, heptagonal
    and octagonal numbers, that have four digits.
    :return: list of lists of polygonal numbers
    """
    triangles = []
    squares = []
    pentagonals = []
    hexagonals = []
    heptagonals = []
    octagonals = []

    i = 2
    flag = True

    while flag:
        flag = False

        current = i * (i + 1) // 2
        if len(str(current)) == 4:
            triangles.append(current)
            flag = True
        elif len(str(current)) < 4:
            flag = True

        current = i ** 2
        if len(str(current)) == 4:
            squares.append(current)
            flag = True

        current = i * (3 * i - 1) // 2
        if len(str(current)) == 4:
            pentagonals.append(current)
            flag = True

        current = i * (2 * i - 1)
        if len(str(current)) == 4:
            hexagonals.append(current)
            flag = True

        current = i * (5 * i - 3) // 2
        if len(str(current)) == 4:
            heptagonals.append(current)
            flag = True

        current = i * (3 * i - 2)
        if len(str(current)) == 4:
            octagonals.append(current)
            flag = True

        i += 1

    return [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]


def find_cycle(polygonals):
    """
    Finds the only ordered set of six cyclic 4-digit numbers for which each polygonal type
    is represented by a different number in the set.
    :param polygonals: list of lists of 4-digit polygonal type numbers
    :return:
    """
    # index 0 is always used, because we start by choosing the triangle number
    not_used_indexes = {1, 2, 3, 4, 5}

    # try each triangle number
    for tr in polygonals[0]:
        for n in not_used_indexes:
            for i in range(len(polygonals[n])):
                if (tr % 100) == (polygonals[n][i] // 100):
                    # found second number of some polygonal type
                    not_used_4 = not_used_indexes - {n}
                    for o in not_used_4:
                        for j in range(len(polygonals[o])):
                            if (polygonals[n][i] % 100) == (polygonals[o][j] // 100):
                                # found third number of some polygonal type
                                not_used_3 = not_used_4 - {o}
                                for p in not_used_3:
                                    for k in range(len(polygonals[p])):
                                        if (polygonals[o][j] % 100) == (polygonals[p][k] // 100):
                                            # found fourth number of some polygonal type
                                            not_used_2 = not_used_3 - {p}
                                            for q in not_used_2:
                                                for m in range(len(polygonals[q])):
                                                    if (polygonals[p][k] % 100) == (polygonals[q][m] // 100):
                                                        # found fifth number of some polygonal type
                                                        last_index = list(not_used_2 - {q})[0]
                                                        for s in range(len(polygonals[last_index])):
                                                            if (polygonals[q][m] % 100) == (
                                                                    polygonals[last_index][s] // 100):
                                                                # try cycling the set to the first triangle number
                                                                if (polygonals[last_index][s] % 100) == (tr // 100):
                                                                    return [tr, polygonals[n][i], polygonals[o][j],
                                                                            polygonals[p][k], polygonals[q][m],
                                                                            polygonals[last_index][s]]


print(sum(find_cycle(generate_four_digit_numbers())))
