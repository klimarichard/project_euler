from algorithms import divisors


def find_largest_prime_factor(n):
    """
    Find the largest prime factor of given number.
    :param n: an integer
    :return: largest prime factor of n
    """
    divs = divisors(n)

    current_divs = divs.copy()
    i = len(divs) - 2

    while len(current_divs) > 2:
        current = divs[i]
        current_divs = [x for x in divs if current % x == 0]
        i -= 1

    return current_divs[1]


print(find_largest_prime_factor(600851475143))
