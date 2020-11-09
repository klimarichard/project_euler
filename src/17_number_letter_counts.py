import inflect


def words_for_numbers(upper, lower=1):
    """
    Returns list of numbers written out in words in given range.
    :param upper: upper bound
    :param lower: optional lower bound (default = 1)
    :return: list of numbers from range written out in words
    """
    words = []
    p = inflect.engine()

    for i in range(lower, upper + 1):
        words.append(p.number_to_words(i))

    return words


def count_letters(strings):
    """
    Counts letters in given list of strings (spaces and hyphens excluded).
    :param strings: list of strings
    :return: number of letters in strings
    """
    return len([x for i in range(len(strings)) for x in strings[i] if x != ' ' and x != '-'])


print(count_letters(words_for_numbers(1000)))
