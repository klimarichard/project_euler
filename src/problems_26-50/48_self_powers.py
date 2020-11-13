powers = [i ** i for i in range(1, 1001)]

print(sum(powers) % (10 ** 10))
