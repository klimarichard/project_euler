from algorithms import palindrome


def palindrome_products(a, b):
    """
    Returns list of palindromic products of numbers in given range.
    :param a: lower bound
    :param b: upper bound
    :return: list of palindromic products
    """
    return [x * y for x in range(a, b) for y in range(x, b) if palindrome(x * y)]


print(max(palindrome_products(101, 1001)))
