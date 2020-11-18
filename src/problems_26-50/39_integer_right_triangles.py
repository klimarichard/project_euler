def find_maximum_radius(n):
    """
    Find radius of a right triangle in given range, for which is the number of right
    triangles with integer sides maximal.
    :param n: upper bound
    :return: radius of such right triangle
    """
    max_n = 11
    max_solutions = 0

    for i in range(12, n + 1):
        current_solutions = [(a, b, i - (a + b)) for a in range(1, i) for b in range(a, i - (a + 1))
                             if a * a + b * b == (i - (a + b)) * (i - (a + b))]

        if len(current_solutions) > max_solutions:
            max_n = i
            max_solutions = len(current_solutions)

    return max_n


print(find_maximum_radius(1000))
