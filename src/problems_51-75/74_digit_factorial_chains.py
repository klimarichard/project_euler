from algorithms import fact


def find_k_chains(k, n):
    """
    Find all numbers in given range with digit factorial chain of given length.
    :param k: desired length of the chain
    :param n: upper bound
    :return: list of numbers with chains of length k
    """
    chain_lengths = [-1 for _ in range((len(str(n)) + 2) * fact(9))]

    for i in range(n):
        if chain_lengths[i] != -1:
            continue

        current_chain = [i]

        # current factorial sum
        fds = sum([fact(n) for n in [int(x) for x in str(i)]])

        found = False
        while fds not in current_chain:
            # we already know the length of the cycle for the next number in the sequence,
            # so we write the values for current chain
            if chain_lengths[fds] != -1:
                found = True
                for j in range(len(current_chain)):
                    chain_lengths[current_chain[j]] = len(current_chain) - j + chain_lengths[fds]

                break

            current_chain.append(fds)
            fds = sum([fact(n) for n in [int(x) for x in str(fds)]])

        # if this was a completely new chain, write the chain lengths
        # for each element in the chain
        if not found:
            r = current_chain.index(fds)
            for j in range(r):
                chain_lengths[current_chain[j]] = len(current_chain) - j
            for j in range(r, len(current_chain)):
                chain_lengths[current_chain[j]] = len(current_chain) - r

    result = [x for x in range(n) if chain_lengths[x] == k]

    return result


print(len(find_k_chains(60, 1000000)))
