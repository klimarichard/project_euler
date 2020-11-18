# Algorithms
The `algorithms.py` file contains reusable algorithms and generators used throughout
the solutions.
Within descriptions of some algorithms are time references for measuring the algorithms
computing power on some small and some large data.

- [Mathematical algorithms](#mathematical-algorithms)
- [List algorithms](#list-algorithms)
- [String algorithms](#string-algorithms)
- [Generators](#generators)


## Mathematical algorithms

### Collatz sequence
The Collatz sequence generator is just rewritten mathematical definition:

<p align="center">
<code>n -> n/2</code>, if <code>n</code> is even,<br>
<code>n -> 3n + 1</code>, if <code>n</code> is odd.
</p>

##### Implementation
```python
def collatz(n):
    seq = [n]

    while seq[-1] != 1:
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)

    return seq
```


### Continuous fraction
This algorithm computes the continuous fraction for square root of given number, that
cannot be a square.
##### Implementation
```python
def continuous_fraction(n):
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
```


### Divisors
The `divisors` algorithm returns all divisors of given integer.
##### Implementation
```python
import math


def divisors(n):
    divs = [x for x in range(1, round(math.sqrt(n)) + 1) if n % x == 0]
    divs += [n // x for x in divs]
    divs.sort()

    return divs
```
##### Reference times
`divisors(979)` finished in `4.768` μs\
`divisors(2 ** 20)` finished in `0.059` ms


### Eratosthenes sieve
The sieve of Eratosthenes finds prime numbers up to given upper boundary.
The implementation uses Python sets for faster subtraction of non-primes, however
it returns a sorted list.
##### Implementation
```python
def eratosthenes(number):
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
```
##### Reference times
`eratosthenes(10000)` finished in `0.821` ms\
`eratosthenes(10000000)` finished in `1.421` s


### Euler's totient function
Computes the value of Euler's totient function for given number. By definition of
Euler's totient function, it holds:

<p align="center">
<code>φ(n) = p<sub>1</sub><sup>k<sub>1</sub> - 1</sup> * (p<sub>1</sub> - 1) *
p<sub>2</sub><sup>k<sub>2</sub> - 1</sup> * (p<sub>2</sub> - 1) * ... *
p<sub>r</sub><sup>k<sub>r</sub> - 1</sup> * (p<sub>r</sub> - 1)</code>, for
<code>n = p<sub>1</sub><sup>k<sub>1</sub></sup> *
p<sub>2</sub><sup>k<sub>2</sub></sup> * ... *
p<sub>r</sub><sup>k<sub>r</sub></sup></code>, where <code>p<sub>1</sub>,
p<sub>2</sub>, ..., p<sub>r</sub></code> are pairwise distinct primes dividing
<code>n</code>.
</p>

##### Implementation
```python
from algorithms import prime_factors_list


def totient(n):
    phi = 1
    divs = prime_factors_list(n)

    for p in range(len(divs)):
        phi *= ((divs[p][0] ** (divs[p][1] - 1)) * (divs[p][0] - 1))

    return phi
```


### Factorial
The factorial generator uses recursion for finding the solution, following the
mathematical definition.
##### Implementation
```python
def fact(n: int):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
```
##### Reference times
`fact(500)` finished in `0.180` ms\
`fact(800)` finished in `0.304` ms


### Greatest common divisor
The GCD algorithm uses the basic recursive definition of GCD.
##### Implementation
```python
def gcd(a, b):
    if b > a:
        a, b = b, a

    if b == 0:
        return a
    else:
        return gcd(a % b, b)
```


### Hexagonality
This function determines, whether given number `n` is hexagonal, so if there is some
`k`, that `n = k(2k - 1)`. This test was found on Wikipedia.
##### Implementation
```python
import math


def is_hexagonal(n):
    if (1 + math.sqrt(8 * n + 1)) % 4 == 0:
        return True
    else:
        return False
```


### Lowest common multiplier
The LCM algorithm computes lowest common multiplier of two or more integers.
##### Implementation
```python
from algorithms import gcd


def lcm(a, b, *args):
    g = gcd(a, b)
    mul = (a * b) // g

    for i in range(len(args)):
        g = gcd(mul, args[i])
        mul = (args[i] * mul) // g

    return mul
```


### Next permutation
This algorithm finds next lexicographical permutation from the one given as input.
If input permutation is the lexicographically last, it returns `None`.
##### Implementation
```python
def next_permutation(current_perm):
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
```


### Palindrome
Finds, if given number is palindromic.
##### Implementation
```python
def palindrome(n):
    if str(n) == "".join(reversed(str(n))):
        return True
    else:
        return False
```


### Pentagonality
This function determines, whether given number `n` is pentagonal, so if there is some
`k`, that `n = k(3k - 1) / 2`. This test was found on Wikipedia.
##### Implementation
```python
import math


def is_pentagonal(n):
    if (1 + math.sqrt(24 * n + 1)) % 6 == 0:
        return True
    else:
        return False
```


### Primality test
This function tests, if the given number is a prime number.
##### Implementation
```python
def is_prime(n):
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
```
##### Reference times
`is_prime((2 ** 31) - 1)` finished in `6.712` ms\
`is_prime(39916801 ** 2)` finished in `5.803` s


### Prime factors
This algorithm finds all distinct prime factors of given number.
##### Implementation I
```python
import math


def prime_factors(n):
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
```
##### Implementation II
```python
import math


def prime_factors_list(n):
    i = 2
    a = []

    while i < math.sqrt(n):
        while n % i == 0:
            n = n // i
            a.append(i)
        i += 1

    if n > 1:
        a.append(n)

    a = sorted(a)
    result = []
    for k in set(a):
        result.append((k, count_item(a, k)))

    return result
```


### Sum of digits
This algorithm finds digit-wise sum of given integer.
##### Implementation
```python
def sum_of_digits(n):
    digits = [int(d) for d in str(n)]

    return sum(digits)
``` 


### Sum of proper divisors
This algorithms finds sum of all proper divisors of given integer.
##### Implementation
```python
def sum_of_proper_divisors(divisors):
    return sum(divisors[:-1])
```

---

## List algorithms

### Count item
Counts elements, that are equal to given item in given list.
##### Implementation
```python
def count_item(ls, item):
    if item not in ls:
        return 0

    ls = sorted(ls)
    count = 1
    item_index = ls.index(item)
    i = 1

    while item_index + i < len(ls) and ls[item_index + i] == item:
        count += 1
        i += 1

    return count
```


### Distinct elements
Finds, if all elements of given list are pairwise distinct.
##### Implementation
```python
def distinct(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return False

    return True
```


### Product of elements
Finds product of all elements in a list.
##### Implementation
```python
def product(ls):
    result = 1

    for i in range(len(ls)):
        result *= ls[i]

    return result
```

---

## String algorithms

### Alphabetical value
Returns alphabetical value of a word, e. g. `SKY = 19 + 11 + 25 = 55`.
##### Implementation
```python
def get_alphabetical_value(name):
    values = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = 0

    for i in range(len(name)):
        value += values.index(name[i])

    return value
```


### Delete quotes
Deletes quotes surrounding a string from all strings in a list.
##### Implementation
```python
def delete_quotes(names):
    return [name[1:-1] for name in names]
```


### Find duplicates
This algorithm finds all characters, that appear more than once in a string.
##### Implementation
```python
def duplicates(s):
    dups = set()
    for i in range(1, len(s)):
        if s[i] in s[0:i]:
            dups |= {s[i]}

    dups = sorted(dups)

    return dups
```

---

## Generators

### Fibonacci generator
This generator generates all Fibonacci numbers.
##### Implementation
```python
def gen_fibs():
    f1, f2 = 1, 2
    while True:
        yield f1
        f1, f2 = f2, f1 + f2
```
##### Reference times
`gen_fibs()` for `1000000` iterations finished in `0.256` s


### Naturals generator
This generator generates all natural numbers.
##### Implementation
```python
def gen_naturals():
    current = 1
    while True:
        yield current
        current += 1
```
##### Reference times
`gen_naturals()` for `1000000` iterations finished in `0.119` s


### Powers generator
This generator generates all numbers to the power of n.
##### Implementation
```python
def gen_powers(n):
    current = 1
    while True:
        yield current ** n
        current += 1
```
##### Reference times
`gen_powers(2)` for `1000000` iterations finished in `0.275` s
`gen_powers(10)` for `1000000` iterations finished in `0.360` s
`gen_powers(0.5)` for `1000000` iterations finished in `0.176` s