def delete_quotes(names):
    """
    Delete quotes from names in a list of names.
    :param names: list of names
    :return: list of raw names
    """
    return [name[1:-1] for name in names]


def get_alphabetical_value(name):
    """
    Returns alphabetical value of a given name.
    :param name: a string
    :return: alphabetical value of name
    """
    values = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = 0

    for i in range(len(name)):
        value += values.index(name[i])

    return value


names = []

with open('../res/p022_names.txt', "r") as f:
    line = f.readline()

    while line:
        names = names + line.split(',')
        line = f.readline()

names = delete_quotes(names)
names.sort()

names_score = 0

for i in range(len(names)):
    names_score += (get_alphabetical_value(names[i]) * (i + 1))

print(names_score)
