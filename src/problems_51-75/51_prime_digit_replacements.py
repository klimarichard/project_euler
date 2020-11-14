from algorithms import duplicates, eratosthenes


def replace_duplicates(n):
    """
    Replaces duplicate digits in given number with another digit.
    :param n: an integer
    :return: list of all replacements, that are also primes (possibly list of lists)
    """
    n = str(n)
    dups = duplicates(n)
    replacements = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for duplicate in dups:
        current = list(filter(lambda x: x in primes, [int(n.replace(duplicate, k)) for k in numbers]))
        replacements.append(current)

    return replacements


# find all primes, where numbers can be replaced
# upper bound is too arbitrary, but I couldn't find it analytically
primes = [n for n in eratosthenes(1000000) if len(str(n)) - len(set(str(n))) >= 3]

i = 0
flag = True

while flag:
    replacements = replace_duplicates(primes[i])
    for ls in replacements:
        if len(ls) == 8:
            print(ls[0])
            flag = False
            break

    i += 1
