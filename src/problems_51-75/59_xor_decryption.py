def decrypt_chars(encrypted):
    """
    Decrypt the text encrypted with XOR encryption.
    :param encrypted: list of encrypted chars
    :return: decrypted string
    """
    decrypted = ''

    # range for ordinals of English letters
    english_letters = range(97, 123)

    key_first = set()
    key_second = set()
    key_third = set()

    # checks if XORed values of encrypted ordinals are all
    # common English letters for first letter of the key,
    # so for letters on positions 0, 3, 6, ... in the encrypted
    for c in english_letters:
        for i in range(0, len(encrypted), 3):
            key_first.add(c)
            if not is_common_english(encrypted[i], key=c):
                key_first.remove(c)
                break

    # checks if XORed values of encrypted ordinals are all
    # common English letters for second letter of the key,
    # so for letters on positions 1, 4, 7, ... in the encrypted
    for c in english_letters:
        for i in range(1, len(encrypted), 3):
            key_second |= {c}
            if not is_common_english(encrypted[i], key=c):
                key_second -= {c}
                break

    # checks if XORed values of encrypted ordinals are all
    # common English letters for third letter of the key,
    # so for letters on positions 2, 5, 8, ... in the encrypted
    for c in english_letters:
        for i in range(2, len(encrypted), 3):
            key_third |= {c}
            if not is_common_english(encrypted[i], key=c):
                key_third -= {c}
                break

    for i in range(len(key_first)):
        for j in range(len(key_second)):
            for k in range(len(key_third)):
                key = chr(list(key_first)[i]) + chr(list(key_second)[j]) + chr(list(key_third)[k])

                for n in range(0, len(encrypted), 3):
                    decrypted += decrypt(encrypted[n:n+3], key)

    return decrypted


def is_common_english(c, key=None):
    """
    Checks, if given ordinal of a char, optionally XORed by given key,
    is a common English letter.
    :param c: an ordinal number of char
    :param key: optional ordinal number of a key
    :return:
    """
    if key is not None:
        c ^= key

    # 32 -> space, 33-47 -> !, ", #, ..., 48-57 -> 0, 1, 2, ...,
    # 58-64 -> :, ;, <, ..., 65-90 -> A, B, C, ...
    if 31 < c < 91:
        return True
    # 91, 93 -> [, ]
    elif c == 91 or c == 93:
        return True
    # 97-122 -> a, b, c, ...
    elif 96 < c < 123:
        return True
    else:
        return False


def decrypt(lc, key):
    """
    Decrypt a XOR encrypted chars with given key.
    :param lc: list of encrypted chars
    :param key: a string with decryption key
    :return: decrypted string
    """
    if len(lc) % len(key) != 0:
        print('Decryption key cannot be mapped on given list of chars:')
        print('  - length of encrypted list: {}'.format(len(lc)))
        print('  - length of decryption key: {}'.format(len(key)))
        print('  - modulus: {}'.format(len(lc) % len(key)))
        return None
    else:
        return ''.join(chr(c ^ ord(k)) for c, k in zip(lc, key))


encrypted = []

with open('../../res/p059_cipher.txt', 'r') as f:
    encrypted += f.read().strip().split(',')

encrypted = [int(x) for x in encrypted]


decrypted = decrypt_chars(encrypted)

print(sum(list(map(ord, decrypted))))
print(decrypted)
