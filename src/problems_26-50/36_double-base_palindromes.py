from algorithms import palindrome


def find_double_based_palindromes(n):
    """
    Find double-based palindromes in given range.
    :param n: upper bound
    :return: list of all double-based palindromes
    """
    dbp = []

    for i in range(n):
        if i % 10 == 0:
            continue
        if palindrome(i):
            if palindrome(bin(i)[2:]):
                dbp.append(i)

    return dbp


print(sum(find_double_based_palindromes(1000000)))
