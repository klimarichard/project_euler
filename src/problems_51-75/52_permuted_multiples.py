from algorithms import gen_naturals


def same_digits(x, x2, *args):
    """
    Finds, if the given numbers all contain the same digits
    :param x: first integer
    :param x2: second integer
    :param args: optional more integers
    :return: True, if all numbers contain the same digits, False, otherwise
    """
    x = set(str(x))
    x2 = set(str(x2))

    if len(x) != len(x2):
        return False
    elif len(x - x2) != 0:
        return False
    else:
        for i in range(len(args)):
            x_i = set(str(args[i]))
            if len(x) != len(x_i):
                return False
            elif len(x_i - x) != 0:
                return False

        return True


N = gen_naturals()
current = next(N)

while not (same_digits(current, 2 * current, 3 * current,
                       4 * current, 5 * current, 6 * current)):
    current = next(N)

print(current)
