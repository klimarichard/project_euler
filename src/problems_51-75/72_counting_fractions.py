from algorithms import totient


fractions = 0

for i in range(2, 1000001):
    fractions += totient(i)

print(fractions)
