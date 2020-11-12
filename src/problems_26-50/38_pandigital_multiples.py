def find_maximum_pandigital_multiple():
    """
    Finds the maximum concatenated product of an integer with (1, 2, ..., n), where n > 1,
    which is 1 to 9 pandigital.
    :return: maximum pandigital concatanated product
    """
    # from the task description, we know, that 9 x (1, 2, 3, 4, 5) produces this number,
    # so we are only interested in larger numbers.
    max_pandigital = [9, 1, 8, 2, 7, 3, 6, 4, 5]

    # we are only interested in numbers starting with 91, 918 or 9182 respectively, since we already
    # have a max starting with 9182
    # also, 5-digit numbers cannot produce a 9-digit concatenated product
    i_to_examine = list(range(91, 100)) + list(range(918, 987)) + list(range(9182, 9876))

    for i in i_to_examine:
        n = 1
        index = 0
        flag = True
        current_pan = []
        already_larger = False

        while flag:
            current_digits = [int(x) for x in str(i * n)]
            if not distinct(current_pan + current_digits):
                break

            # if we have already found a greater digit in higher order,
            # we can skip this part
            if not already_larger:
                for j in range(index, len(current_digits)):
                    if max_pandigital[j] > current_digits[j]:
                        flag = False
                    elif max_pandigital[j] < current_digits[j]:
                        already_larger = True
                        break

            # append current product to concatenation
            if flag and len(current_pan) < 9:
                index += len(current_digits)
                current_pan += current_digits
                n += 1

        # we can only reach this code, when we have found a new maximum
        # we also have to make sure, that the current number doesn't contain a 0
        if len(current_pan) == 9 and 0 not in current_pan:
            max_pandigital = current_pan

    return max_pandigital


def distinct(digits):
    """
    Finds, if all digits in given list are pairwise distinct.
    :param digits: list of digits
    :return: True, if all digits are pairwise distinct, False, otherwise
    """
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i] == digits[j]:
                return False

    return True


print(int("".join([str(x) for x in find_maximum_pandigital_multiple()])))
