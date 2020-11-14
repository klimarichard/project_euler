from algorithms import gen_fibs


f = gen_fibs()
next_fib = next(f)
sum = 0

while next_fib < 4000000:
    if next_fib % 2 == 0:
        sum += next_fib

    next_fib = next(f)

print(sum)
