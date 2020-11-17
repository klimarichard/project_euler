def compute_nth_iteration(n):
    """
    Computes n-th iteration of continued fraction for e,
    2 + (1 / (1 + 1 / (2 + 1 / (1 + 1 / (1 + 1 / (4 + ...))))))
    :param n: an integer
    :return: numerator and denominator of n-th iteration
    """
    # generating sequence for continued fraction of e
    # [1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]
    e_sequence = [1 for _ in range(n)]
    for i in range(n):
        if i % 3 == 1:
            e_sequence[i] = (i // 3 + 1) * 2

    num = 1
    denom = e_sequence[n - 1]

    # we have to compute the fraction from inside out
    for i in range(n - 1):
        num = denom * e_sequence[n - (i + 2)] + num

        num, denom = denom, num

    # add the final two
    num = denom * 2 + num

    return num, denom


num, _ = compute_nth_iteration(99)

print(sum([int(x) for x in str(num)]))
