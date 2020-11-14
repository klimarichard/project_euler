def find_combinations(upper, lower=1, threshold=1):
    """
    Find all combinatoric selections within given range.
    :param upper: upper bound
    :param lower: optional lower bound (default=1)
    :param threshold: optional, only list selections greater than threshold (default=1)
    :return: list of combinatoric selections
    """
    selections = []

    for n in range(lower, upper + 1):
        for k in range(1, n + 1):
            current = factorials[n] // (factorials[k] * factorials[n - k])
            if current > threshold:
                selections.append(current)

    return selections


factorials = [1, 1]

# building the list of factorials, so we don't need to recompute them every time
for i in range(2, 101):
    factorials.append(i * factorials[-1])

print(factorials)

print(len(find_combinations(100, lower=23, threshold=1000000)))
