import math


def divisors(n):
    """
    Returns list of divisors of given number.
    :param n: an integer
    :return: list of divisors
    """
    divs = [x for x in range(1, round(math.sqrt(n)) + 1) if n % x == 0]
    divs += [n // x for x in divs]
    divs.sort()

    return divs


NUMBER = 600851475143

divs = divisors(NUMBER)

current_divs = divs.copy()
i = len(divs) - 2

while len(current_divs) > 2:
    current = divs[i]
    current_divs = [x for x in divs if current % x == 0]
    i -= 1

print(current_divs[1])
