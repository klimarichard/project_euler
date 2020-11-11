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


def palindrome(n):
    """
    Finds, if given number is palindromic (with no leading zeros).
    :param n: an integer (in any base)
    :return: True, if given number is palindromic, False, otherwise
    """
    if str(n) == "".join(reversed(str(n))):
        return True
    else:
        return False


print(sum(find_double_based_palindromes(1000000)))
