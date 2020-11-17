"""
This file contains useful reusable algorithms from all solutions.
"""
import math


# -----------------------
# MATHEMATICAL ALGORITHMS
# -----------------------

def collatz(n):
    """
    Returns Collatz sequence for given number.
    :param n: an integer
    :return: Collatz sequence for given integer
    """
    seq = [n]

    while seq[-1] != 1:
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)

    return seq


def continuous_fraction(n):
    """
    Computes a continuous fraction for square root of given number.
    :param n: a positive integer
    :return: a list comprising of a_0 and a list containing the period
             of the repeating a_n
    """
    period = []

    a0 = int(n ** 0.5)
    fst_rem = [1, a0]
    fst_rem_val = 1 / ((n ** 0.5) - a0)

    a1 = int(fst_rem_val)
    period.append(a1)
    # already reciprocal
    rem = [n - (a0 ** 2), - (a0 - ((n - (a0 ** 2)) * a1))]

    while rem != fst_rem:
        an = int(rem[0] / ((n ** 0.5) - rem[1]))
        period.append(an)

        denom = (n - (rem[1] ** 2)) // rem[0]
        num = rem[1] - (an * denom)
        # already reciprocal
        rem = [denom, -num]

    return a0, period


def divisors(n):
    """
    Returns list of divisors of given number.
    :param n: an integer
    :return: list of divisors
    """
    divs = [x for x in range(1, round(math.sqrt(n)) + 1) if n % x == 0]
    divs += [n // x for x in divs]
    divs.sort()

    return divs


def eratosthenes(number):
    """
    Returns a list of all prime numbers from 2 to given number
    :param number: upper boundary for generating prime numbers
    :return: list containing all prime numbers from 2 to given number
    """
    a = set(range(3, number + 1, 2))
    a |= {2}
    p = 3

    while p <= number ** 0.5:
        a -= set(range(p * p, number + 1, 2 * p))
        p += 2

        # it is pointless to examine numbers that aren't primes themselves
        while p not in a:
            p += 2

    a = sorted(a)

    return a


def fact(n: int):
    """
    Returns factorial of given integer.
    :param n: an integer
    :return: factorial of n
    """
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def gcd(a, b):
    """
    Computes greatest common divisor using the basic Euclidean algorithm.
    :param a: first integer
    :param b: second integer
    :return: GCD(a, b)
    """
    if b > a:
        a, b = b, a

    if b == 0:
        return a
    else:
        return gcd(a % b, b)


def is_hexagonal(n):
    """
    Finds, if given integer is a hexagonal number, so if there exist some k,
    that n = k(2k - 1)
    :param n: an integer
    :return: True, if n is a hexagonal number, False otherwise
    """
    # this test for hexagonality was found online
    if (1 + math.sqrt(8 * n + 1)) % 4 == 0:
        return True
    else:
        return False


def is_pentagonal(n):
    """
    Finds, if given integer is a pentagonal number, so if there exist some k,
    that n = k(3k - 1) / 2.
    :param n: an integer
    :return: True, if n is a pentagonal number, False otherwise
    """
    # this test for pentagonality was found online
    if (1 + math.sqrt(24 * n + 1)) % 6 == 0:
        return True
    else:
        return False


def is_prime(n):
    """
    Finds, if given integer is a prime number.
    :param n: an integer
    :return: True, if n is prime, False, otherwise
    """
    if n == 1:
        return False
    if n == 2:
        return True

    i = 3
    while i < int(n ** 0.5) + 1:
        if n % i == 0:
            return False
        i += 2

    return True


def lcm(a, b, *args):
    """
    Returns lowest common multiplier of given numbers.
    :param a: first integer
    :param b: second integer
    :param args: optional more integers
    :return: LCM of all given integers
    """
    g = gcd(a, b)
    mul = (a * b) // g

    for i in range(len(args)):
        g = gcd(mul, args[i])
        mul = (args[i] * mul) // g

    return mul


def next_permutation(current_perm):
    """
    Generates next permutation after given one.
    :param current_perm: a list with current permutation
    :return: next permutation after current_perm or None, if current_perm is the last
    """
    # find the largest index k such that current_perm[k] < current_perm[k + 1]
    # if there is no such index, current_perm is the last permutation
    k = len(current_perm) - 2

    while k != -1:
        if current_perm[k] < current_perm[k + 1]:
            break
        else:
            k -= 1

    if k == -1:
        return None

    # find the largest index l greater than k such that current_perm[k] < current_perm[l]
    l = len(current_perm) - 1

    while l != k:
        if current_perm[k] < current_perm[l]:
            break
        else:
            l -= 1

    # swap the values of current_perm[k] and current_perm[l]
    temp = current_perm[k]
    current_perm[k] = current_perm[l]
    current_perm[l] = temp

    # reverse the sequence from current_perm[k + 1] up to and including a[n]
    for i in range(k + 1, (len(current_perm) + (k + 1)) // 2):
        temp = current_perm[i]
        current_perm[i] = current_perm[len(current_perm) - (i - k)]
        current_perm[len(current_perm) - (i - k)] = temp

    return current_perm


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


def prime_factors(n):
    """
    Finds all prime factors of given number.
    :param n: an integer
    :return: set of prime factors of n
    """
    i = 2
    a = set()

    while i < math.sqrt(n) or n == 1:
        if n % i == 0:
            n = n // i
            a.add(i)
            i -= 1
        i += 1

    if n > 1:
        a.add(n)

    return a


def sum_of_digits(n):
    """
    Returns sum of digits of given number.
    :param n: an integer
    :return: sum of digits of n
    """
    digits = [int(d) for d in str(n)]

    return sum(digits)


def sum_of_proper_divisors(divisors):
    """
    Returns sum of proper divisors.
    :param divisors: list of all divisors
    :return: sum of proper divisors
    """
    return sum(divisors[:-1])


# ---------------
# LIST ALGORITHMS
# ---------------

def distinct(numbers):
    """
    Finds, if all numbers in given list are pairwise distinct.
    :param numbers: list of numbers
    :return: True, if all numbers are pairwise distinct, False, otherwise
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return False

    return True


def product(ls):
    """
    Returns product of elements in given list.
    :param ls: a list of numbers
    :return: product of all elements
    """
    result = 1

    for i in range(len(ls)):
        result *= ls[i]

    return result

# -----------------
# STRING ALGORITHMS
# -----------------


def delete_quotes(ls):
    """
    Delete quotes from strings in a list of strings.
    :param ls: list of strings
    :return: list of raw strings
    """
    return [s[1:-1] for s in ls]


def duplicates(s):
    """
    Finds all chars, that appear more than once in given string.
    :param s: a string
    :return: list of chars appearing more than once in s
    """
    dups = set()
    for i in range(1, len(s)):
        if s[i] in s[0:i]:
            dups |= {s[i]}

    dups = sorted(dups)

    return dups


def get_alphabetical_value(word):
    """
    Returns alphabetical value of a given word.
    :param word: a string
    :return: alphabetical value of word
    """
    values = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = 0

    for i in range(len(word)):
        value += values.index(word[i])

    return value

# ----------
# GENERATORS
# ----------


def gen_fibs():
    """
    Generator for Fibonacci numbers.
    :return: next Fibonacci number
    """
    f1, f2 = 1, 2
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


def gen_naturals():
    """
    Generator for natural numbers.
    :return: next natural number
    """
    current = 1
    while True:
        yield current
        current += 1


def gen_powers(n):
    """
    Generator for n-th powers of naturals numbers.
    :param n: power
    :return: next natural number's n-th power
    """
    current = 1
    while True:
        yield current ** n
        current += 1
