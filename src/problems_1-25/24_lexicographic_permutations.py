from itertools import permutations


next_perm = '0123456789'
p = permutations('0123456789')

for i in range(1000000):
    next_perm = next(p)

print("".join(s for s in next_perm))
