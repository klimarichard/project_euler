def fibs(n):
    """
    Generates list of Fibonacci numbers upto given bound.
    :param n: upper bound
    :return: list of Fibonacci numbers lesser than given bound
    """
    if n == 1:
        return [1]

    fib = [1, 2]

    while (fib[-1] + fib[-2]) < n:
        fib.append(fib[-1] + fib[-2])

    return fib


even_fibs = [x for x in fibs(4000000) if x % 2 == 0]

print(sum(even_fibs))
