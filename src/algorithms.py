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

    a = list(a)
    a.sort()

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
        temp = a
        a = b
        b = temp

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


def delete_quotes(names):
    """
    Delete quotes from names in a list of names.
    :param names: list of names
    :return: list of raw names
    """
    return [name[1:-1] for name in names]


def get_alphabetical_value(name):
    """
    Returns alphabetical value of a given name.
    :param name: a string
    :return: alphabetical value of name
    """
    values = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = 0

    for i in range(len(name)):
        value += values.index(name[i])

    return value

