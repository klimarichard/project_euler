from algorithms import delete_quotes, get_alphabetical_value


def find_longest_word(words):
    """
    Find length of the longest word in a list of words.
    :param words: list of words
    :return: lenght of the longest word
    """
    current_longest = 0

    for word in words:
        if len(word) > current_longest:
            current_longest = len(word)

    return current_longest


def find_coded_triangles(n):
    """
    Find coded triangle number lesser than given range.
    :param n: upper bound
    :return: list of coded triangle numbers
    """
    coded_triangle = [1]
    i = 2

    while coded_triangle[-1] < n:
        coded_triangle.append(i * (i + 1) // 2)
        i += 1

    return coded_triangle


words = []

with open('../../res/p042_words.txt', "r") as f:
    line = f.readline()

    while line:
        words = words + line.split(',')
        line = f.readline()

words = delete_quotes(words)
triangles = find_coded_triangles(get_alphabetical_value("".join(['Z' for _ in range(find_longest_word(words))])))

tr_words = 0

for word in words:
    if get_alphabetical_value(word) in triangles:
        tr_words += 1

print(tr_words)
