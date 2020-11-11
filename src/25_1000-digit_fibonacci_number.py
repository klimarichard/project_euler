def find_fibonacci_with_k_digits(k):
    """
    Find the index of the first Fibonacci number with more than k digits.
    :param k: an integer
    :return: index of the first Fibonacci number with more than k digits
    """
    fibs1 = 1
    fibs2 = 1
    i = 3

    while (fibs1 + fibs2) / (10 ** (k - 1)) < 1:
        temp = fibs2
        fibs2 = fibs1 + fibs2
        fibs1 = temp
        i += 1

    return i


print(find_fibonacci_with_k_digits(1000))
