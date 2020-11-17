from algorithms import continuous_fraction, gen_powers


squares = []
gen_squares = gen_powers(2)
current = next(gen_squares)

while current < 10001:
    squares.append(current)
    current = next(gen_squares)

odd_period = 0

for i in range(1, 10001):
    if i not in squares:
        fract = continuous_fraction(i)

        if len(fract[1]) % 2 == 1:
            odd_period += 1

print(odd_period)
