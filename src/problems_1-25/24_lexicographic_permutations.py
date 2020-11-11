def next_permutation(current_perm):
    """
    Generates next permutation after given one.
    :param current_perm: a list with current permutation
    :return: next permutation after current_perm or None, if current_perm is the last
    """
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


def find_nth_permutation(current_perm, n):
    """
    Find permutation that is n steps further in lexicographical ordering after
    given permutation.
    :param current_perm: a list with current permutation
    :param n: an integer
    :return: n-th permutation from current_perm
    """
    for _ in range(n - 1):
        current_perm = next_permutation(current_perm)

    return current_perm


perm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("".join([str(i) for i in find_nth_permutation(perm, 1000000)]))
