# we can see, that the diagonals increase by a basic increment and multiples of 8, so we have
# the upper right diagonal: 1 --> 1 + (2 + 0 * 8) = 3 --> 3 + (2 + 1 * 8) = 13 --> 13 + (2 + 2 * 8) = 31 --> ...
# the upper left diagonal: 1 --> 1 + (4 + 0 * 8) = 5 --> 5 + (4 + 1 * 8) = 17 --> 17 + (4 + 2 * 8) = 37 --> ...
# the lower left diagonal: 1 --> 1 + (6 + 0 * 8) = 7 --> 7 + (6 + 1 * 8) = 21 --> 21 + (6 + 2 * 8) = 43 --> ...
# the lower right diagonal: 1 --> 1 + (8 + 0 * 8) = 9 --> 9 + (8 + 1 * 8) = 25 --> 25 + (8 + 2 * 8) = 49 --> ...
#
# we can therefore compute the diagonals easily without having to compute the whole spiral


from algorithms import is_prime

# starting at 3 × 3 spiral, so we already have 3, 5, 7 for primes and
# 1, 9 for non_primes
primes = 3
all_numbers = 5
i = 1
upper_right, upper_left, lower_left, lower_right = 3, 5, 7, 9

# (4 * i + 1) is the number of diagonal elements
while float(primes / all_numbers) > 0.1:
    upper_right = upper_right + (2 + i * 8)
    upper_left = upper_left + (4 + i * 8)
    lower_left = lower_left + (6 + i * 8)
    lower_right = lower_right + (8 + i * 8)

    all_numbers += 4

    if is_prime(upper_right):
        primes += 1
    if is_prime(upper_left):
        primes += 1
    if is_prime(lower_left):
        primes += 1
    if is_prime(lower_right):
        primes += 1

    i += 1


# 3 × 3 spiral is computed with parameter i = 1,
# 5 × 5 spiral is computed with parameter i = 2,
# 7 × 7 spiral is computed with parameter i = 3,
# ...
# (2n + 1) × (2n + 1) spiral is computed with parameter i = n
print(2 * i + 1)
