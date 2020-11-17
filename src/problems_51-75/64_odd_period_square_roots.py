from algorithms import gcd, gen_powers


def compute_continuous_fraction(n):
    """
    Computes a continuous fraction for square root of given number.
    :param n: a positive integer
    :return: a list comprising of a_0 and a list containing the period
             of the repeating a_n
    """
    period = []

    a0 = int(n ** 0.5)
    fst_rem = [1, a0]
    fst_rem_val = 1 / ((n ** 0.5) - a0)

    a1 = int(fst_rem_val)
    period.append(a1)
    # already reciprocal
    rem = [n - (a0 ** 2), - (a0 - ((n - (a0 ** 2)) * a1))]

    while rem != fst_rem:
        # there is a negative value in the remainder, so we add it in the denominator
        an = int(rem[0] / ((n ** 0.5) - rem[1]))
        period.append(an)

        denom = (n - (rem[1] ** 2)) // rem[0]
        num = rem[1] - (an * denom)
        # already reciprocal
        rem = [denom, -num]

    return a0, period


squares = []
gen_squares = gen_powers(2)
current = next(gen_squares)

while current < 10001:
    squares.append(current)
    current = next(gen_squares)

odd_period = 0

for i in range(1, 10001):
    if i not in squares:
        fract = compute_continuous_fraction(i)

        if len(fract[1]) % 2 == 1:
            odd_period += 1

print(odd_period)
