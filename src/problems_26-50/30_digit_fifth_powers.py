def find_digit_fifth_powers():
    """
    Finds all numbers, that can be written as the sum of fifth powers of their digits.
    :return: list of all such numbers
    """
    digit_fifths = []
    fifth_powers = [i ** 5 for i in range(10)]

    # upper bound is too arbitrary, but I couldn't find it analytically
    for i in range(10, 1000000):
        digits = [int(x) for x in str(i)]

        if sum(digits) % 2 != i % 2:
            continue

        else:
            fifths = [fifth_powers[x] for x in digits]
            if sum(fifths) == i:
                digit_fifths.append(i)

    return digit_fifths


print(sum(find_digit_fifth_powers()))
