from algorithms import sum_of_digits


def find_maximum_digital_sum(a, b):
    """
    Find maximal digital sum considering numbers of the form a^b.
    :param a: upper bound for a
    :param b: upper bound for b
    :return: a, b with maximal digital sum
    """
    max_ab = 0, 0
    max_sum = 0

    for i in range(1, a):
        for j in range(1, b):
            current = sum_of_digits(i ** j)
            if current > max_sum:
                max_ab = i, j
                max_sum = current

    return max_ab


largest_sum = find_maximum_digital_sum(100, 100)

print(sum_of_digits(largest_sum[0] ** largest_sum[1]))
