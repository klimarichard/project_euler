from algorithms import product


def find_desired_digits():
    """
    Find digits on decimal places 1, 10, 100, 1000, 10000, 100000 and 1000000 in
    Champerpowne's constant.
    :return: list of desired digits
    """
    indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]
    champerpowne = [0]
    i = 1

    while len(champerpowne) < 1000001:
        digits = [int(x) for x in str(i)]

        champerpowne += digits
        i += 1

    return [champerpowne[i] for i in indexes]


print(product(find_desired_digits()))
