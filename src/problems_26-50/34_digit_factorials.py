def find_digit_factorials():
    """
    Find all numbers which are equal to the sum of the factorial of their digits.
    :return: list of all such numbers
    """
    df = []
    factorials = [fact(i) for i in range(10)]

    # upper bound is arbitrary, but I couldn't find it analytically
    for i in range(10, 1000000):
        fact_digits = [factorials[int(x)] for x in str(i)]
        if sum(fact_digits) == i:
            df.append(i)

    return df


def fact(n):
    """
    Computes factorial of given number.
    :param n: an integer
    :return: a factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(sum(find_digit_factorials()))
