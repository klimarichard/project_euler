#  1 = 1
#  2 = 2
#  3 = 3
#  4 = 2 * 2
#  5 = 5
#  6 = 2 * 3
#  7 = 7
#  8 = 2 * 2 * 2
#  9 = 3 * 3
# 10 = 2 * 5
# 11 = 11
# 12 = 2 * 2 * 3
# 13 = 13
# 14 = 2 * 7
# 15 = 3 * 5
# 16 = 2 * 2 * 2 * 2
# 17 = 17
# 18 = 2 * 3 * 3
# 19 = 19
# 20 = 2 * 2 * 5
# For the number to be divisible by all, it has to satisfy all these factorizations (it is the LCM problem),
# so its factorization has to contain 2^4, 3^2 and all other primes upto 20.

print(2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
