# we can see, that the diagonals increase by a basic increment and multiples of 8, so we have
# the lower right diagonal: 1 --> 1 + (2 + 0 * 8) = 3 --> 3 + (2 + 1 * 8) = 13 --> 13 + (2 + 2 * 8) = 31 --> ...
# the lower left diagonal: 1 --> 1 + (4 + 0 * 8) = 5 --> 5 + (4 + 1 * 8) = 17 --> 17 + (4 + 2 * 8) = 37 --> ...
# the upper left diagonal: 1 --> 1 + (6 + 0 * 8) = 7 --> 7 + (6 + 1 * 8) = 21 --> 21 + (6 + 2 * 8) = 43 --> ...
# the upper right diagonal: 1 --> 1 + (8 + 0 * 8) = 9 --> 9 + (8 + 1 * 8) = 25 --> 25 + (8 + 2 * 8) = 49 --> ...
#
# we can therefore compute all diagonals of 1001 by 1001 spiral and sum their numbers

def compute_diagonals_for_spiral(n):
    """
    Computes all half-diagonals of a n by n spiral of numbers.
    :param n: a dimension of the spiral
    :return: four lists of half-diagonals of the spiral
    """
    lower_right, lower_left, upper_left, upper_right = [1], [1], [1], [1]

    for i in range(n // 2):
        lower_right.append(lower_right[-1] + (2 + i * 8))
        lower_left.append(lower_left[-1] + (4 + i * 8))
        upper_left.append(upper_left[-1] + (6 + i * 8))
        upper_right.append(upper_right[-1] + (8 + i * 8))

    return lower_right, lower_left, upper_left, upper_right


diags = compute_diagonals_for_spiral(1001)
# sum of all diagonals - 3, because the leading one is counted 4 times
print(sum(diags[0]) + sum(diags[1]) + sum(diags[2]) + sum(diags[3]) - 3)
