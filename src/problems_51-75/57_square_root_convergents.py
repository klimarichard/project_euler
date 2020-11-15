from algorithms import gcd


def compute_nth_iteration(n):
    """
    Computes n-th iteration of continued fraction for sqrt(2),
    1 + (1 / (2 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))))
    :param n: an integer
    :return: numerator and denominator of n-th iteration
    """
    num = 1
    denom = 2

    # we have to compute the fraction from inside out
    for i in range(n - 1):
        num = denom * 2 + num

        num, denom = denom, num

    # add the final one
    num = denom + num

    return num, denom


result = 0

for i in range(1000):
    num, denom = compute_nth_iteration(i + 1)
    if len(str(num)) > len(str(denom)):
        result += 1

print(result)
