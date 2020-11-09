def sum_of_digits(n):
    """
    Returns sum of digits of given number.
    :param n: an integer
    :return: sum of digits of n
    """
    digits = [int(d) for d in str(n)]

    return sum(digits)


def fact(n: int):
    """
    Returns factorial of given integer.
    :param n: an integer
    :return: factorial of n
    """
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(sum_of_digits(fact(100)))
