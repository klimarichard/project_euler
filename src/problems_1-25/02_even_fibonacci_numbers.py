from algorithms import gen_fibs


def sum_of_even_fibs(n):
    """
    Returns sum of all even Fibonacci numbers up to given bound.
    :param n: upper bound
    :return: sum of even Fibonacci numbers lesser than n
    """
    f = gen_fibs()
    next_fib = next(f)
    sum = 0

    while next_fib < n:
        if next_fib % 2 == 0:
            sum += next_fib

        next_fib = next(f)

    return sum


print(sum_of_even_fibs(4000000))
