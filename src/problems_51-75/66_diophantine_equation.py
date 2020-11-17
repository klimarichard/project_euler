from algorithms import continuous_fraction, gen_powers


def find_diophantine_solution(D):
    """
    Finds the minimal integer solution in x for Diophantine equation in form
    x^2 - Dy^2 = 1.
    :param D: a parameter of the Diophantine equation
    :return: a minimal integer solution in x
    """
    a0, period = continuous_fraction(D)

    # we need to recurrently find p, such that:
    # p_0 = a_0
    # p_1 = a_0 * a_1 + 1
    # p_n = a_n * p_(n - 1) + p_(n - 2)

    p = [a0, a0 * period[0] + 1]

    for i in range(2, len(period) * 2):
        p.append(period[(i - 1) % len(period)] * p[-1] + p[-2])

    # now let a_(r + 1) be the last element of the period,
    # then according to https://mathworld.wolfram.com/PellEquation.html:
    #  - if r is odd, the minimal solution is x = p_r
    #  - if r is even, the minimal solution is x = p_(2r + 1)
    if len(period) % 2 == 0:
        return p[len(period) - 1]
    else:
        return p[2 * len(period) - 1]


gen_squares = gen_powers(2)
squares = []
current = next(gen_squares)

while current < 1001:
    squares.append(current)
    current = next(gen_squares)

# some value for index 0
solutions = [-1]

for i in range(1, 1001):
    if i not in squares:
        solutions.append(find_diophantine_solution(i))
    else:
        # append some value for easier indexing of the list
        solutions.append(-1)

print(solutions.index(max(solutions)))
