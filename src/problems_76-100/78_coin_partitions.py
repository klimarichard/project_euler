def find_coin_partitions(k):
    """
    Finds first amount of coins, for which the number of ways it can be
    separated into piles is divisible by given integer.
    :param k: divisor
    :return: first number of coins with p(n) divisible by k
    """
    # we can use the generator function and pentagonal number theorem

    # list of moduli of p(n) for n
    mods = [1]
    n = 1
    flag = True

    while flag:
        i = 0
        # pentagonal number
        p = 1
        mods.append(0)

        while p <= n:
            if i % 4 > 1:
                sign = -1
            else:
                sign = 1

            mods[n] += sign * mods[n - p]
            mods[n] %= k
            i += 1

            if i % 2 == 0:
                j = i // 2 + 1
            else:
                j = -((i // 2) + 1)
            # next pentagonal number
            p = j * (3 * j - 1) // 2

        if mods[n] == 0:
            flag = False
        else:
            n += 1

    return n


print(find_coin_partitions(10 ** 6))
