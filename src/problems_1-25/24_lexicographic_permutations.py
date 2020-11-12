from algorithms import next_permutation


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
