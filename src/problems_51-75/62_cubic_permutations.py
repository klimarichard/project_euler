from algorithms import gen_cubes


cubes = gen_cubes()
perms = {}
found = False

while not found:
    current = next(cubes)
    # find largest permutation of current cube (used as key in dictionary)
    current_largest = ''.join(sorted([x for x in str(current)], reverse=True))

    if current_largest not in perms.keys():
        perms[current_largest] = [1, current]
    else:
        perms[current_largest][0] += 1
        if perms[current_largest][0] == 5:
            print(perms[current_largest][1])
            found = True
