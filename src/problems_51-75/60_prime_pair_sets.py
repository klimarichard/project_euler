from algorithms import eratosthenes, is_prime


def find_five_prime_set():
    """
    Finds the lowest five primes, which will produce a prime however permuted
    they are concatenated.
    :return: list of the lowest five primes with that property
    """
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if prime_combination(primes[i], primes[j]):
                for k in range(j + 1, len(primes)):
                    if (prime_combination(primes[i], primes[k]) and
                            prime_combination(primes[j], primes[k])):
                        for m in range(k + 1, len(primes)):
                            if (prime_combination(primes[i], primes[m]) and
                                    prime_combination(primes[j], primes[m]) and
                                    prime_combination(primes[k], primes[m])):
                                for n in range(m + 1, len(primes)):
                                    if (prime_combination(primes[i], primes[n]) and
                                            prime_combination(primes[j], primes[n]) and
                                            prime_combination(primes[k], primes[n]) and
                                            prime_combination(primes[m], primes[n])):
                                        return [primes[i], primes[j], primes[k], primes[m], primes[n]]

    return []


def prime_combination(p, q):
    """
    Finds, if both concatenations pq and qp are primes.
    :param p: first prime
    :param q: second prime
    :return: True, if pq and qp are both primes, False, otherwise
    """
    pq = int(str(p) + str(q))
    qp = int(str(q) + str(p))

    if is_prime(pq) and is_prime(qp):
        return True

    return False


primes = eratosthenes(10000)
# 2 and 5 cannot be a part of the quintuple, since the permutations
# where 2 or 5 would be at the end of the number, cannot be primes
primes.remove(2)
primes.remove(5)

print(sum(find_five_prime_set()))
