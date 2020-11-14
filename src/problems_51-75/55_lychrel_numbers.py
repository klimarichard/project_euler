from algorithms import palindrome


def find_lychrel_numbers(upper, lower=0):
    """
    Find all Lychrel numbers in given range.
    :param upper: upper bound
    :param lower: optional lower bound (default=0)
    :return: list af Lychrel numbers.
    """
    lychrels = []

    for n in range(lower, upper + 1):
        current = n
        i = 0

        for i in range(50):
            current = current + int("".join(reversed(str(current))))
            if palindrome(current):
                break

        if i == 49:
            lychrels.append(n)

    return lychrels


print(len(find_lychrel_numbers(10000)))
