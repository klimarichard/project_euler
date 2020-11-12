from algorithms import distinct, eratosthenes

def find_pandigital_primes():
    """
    Find all pandigital primes.
    :return: list of n-digit pandigital primes
    """
    # there cannot be a 9-digit pandigital prime, since
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45, so all 9-digit pandigital
    # numbers are divisible by 9
    pandigitals = []
    primes = eratosthenes(87654321)

    for p in primes:
        digits = [int(x) for x in str(p)]

        if distinct(digits):
            pandigital = True

            # checking, if the numbers are in range (1, 2, ..., n)
            for i in range(1, len(digits) + 1):
                if i not in digits:
                    pandigital = False
                    break

            if pandigital:
                pandigitals.append(p)

    return pandigitals


print(max(find_pandigital_primes()))
