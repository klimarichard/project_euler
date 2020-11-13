from algorithms import eratosthenes


def find_goldbach_lie():
    """
    Find first composite odd number, that cannot be written as proposed by
    Christian Goldbach.
    :return: first composite odd number violating the Goldbach's conjecture
    """
    # upper bounds are arbitrary, but I couldn't find them analytically
    primes = eratosthenes(10000)
    powers = [x * x for x in range(100)]

    # starting at number 35
    i = 35

    while True:
        found = False
        for p in primes:
            a = [n for n in powers if n == (i - p) // 2]

            if len(a) > 0:
                found = True
                break

        if not found:
            return i

        i += 2

        while i in primes:
            i += 2


print(find_goldbach_lie())
