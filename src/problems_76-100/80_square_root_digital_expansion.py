from decimal import Decimal, getcontext
from algorithms import gen_powers


def compute_decimal_digits(n, k):
    """
    Computes first k digits of square root of n.
    :param n: an integer
    :param k: number of decimal digits
    :return: first k decimal digits of square root of n
    """
    digits = str(Decimal(n).sqrt()).replace('.', '')[:100]
    return map(int, digits)


getcontext().prec = 102

gen_squares = gen_powers(2)
squares = [next(gen_squares)]

while squares[-1] < 100:
    squares.append(next(gen_squares))

sum_of_digits = 0

for i in range(100):
    if i not in squares:
        digits = compute_decimal_digits(i, 100)
        sum_of_digits += sum(digits)

print(sum_of_digits)
