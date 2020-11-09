def sum_of_digits(n):
    """
    Returns sum of digits of given number.
    :param n: an integer
    :return: sum of digits of n
    """
    digits = [int(d) for d in str(n)]

    return sum(digits)


print(sum_of_digits(2 ** 1000))
