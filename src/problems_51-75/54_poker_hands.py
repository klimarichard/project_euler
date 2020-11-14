def parse_hands(line):
    """
    Parse poker hands from a string.
    :param line: a string containing poker hands for two players
    :return: a tuple with the hands of player one and player two
    """
    line_split = line.split(' ')

    return [(c[0], c[-1]) for c in line_split[:5]], [(c[0], c[-1]) for c in line_split[5:]]


def better_hand(player1, player2):
    """
    Determines, if player 1 has better or equal hand than player 2
    :param player1: list of cards of player 1
    :param player2: list of cards of player 2
    :return: True, if player 1 wins or ties in this hand, False otherwise
    """
    p1_hand, p1_values = evaluate_hand(player1)
    p2_hand, p2_values = evaluate_hand(player2)

    if poker_hands[p1_hand] > poker_hands[p2_hand]:
        return True
    elif poker_hands[p1_hand] == poker_hands[p2_hand]:
        if higher_card(p1_values, p2_values):
            return True
        else:
            return False
    else:
        return False


def evaluate_hand(hand):
    """
    Evaluates player's hand by type.
    :param hand: a list with player's cards
    :return: type of hand and high cards (if the hand type is a pair case, the list is
             reorganized, so that the pairs are at the beginning)
    """
    values = sorted([value(val) for (val, _) in hand], reverse=True)
    suits = sorted([suit for (_, suit) in hand])

    hand_type = ''

    # evaluate hands from highest to lowest
    if is_flush(suits):
        if is_straight(values):
            # if high-card is an ace
            if high_card(values) == value('A'):
                hand_type = 'RF'
            else:
                hand_type = 'SF'
        elif is_four_of_a_kind(values):
            hand_type = 'FOK'
        elif is_full_house(values):
            hand_type = 'FH'
        else:
            hand_type = 'F'
    elif is_four_of_a_kind(values):
        hand_type = 'FOK'
    elif is_full_house(values):
        hand_type = 'FH'
    elif is_straight(values):
        hand_type = 'S'
    elif is_three_of_a_kind(values):
        hand_type = 'TOK'
    elif is_two_pairs(values):
        hand_type = 'TP'
    elif is_one_pair(values):
        hand_type = 'OP'
    else:
        hand_type = 'HC'

    # reorganizing hand values, if necessary (pair cases)
    values = reorganize_values(values, hand_type=hand_type)

    return hand_type, values


def is_flush(suits):
    """
    Determines, if these suits form a flush.
    :param suits: suits of a poker hand
    :return: True, if the hand is a flush, False, otherwise
    """
    for i in range(1, len(suits)):
        if suits[0] != suits[i]:
            return False

    return True


def is_straight(values):
    """
    Determines, if these values form a straight.
    :param values: values of a poker hand
    :return: True, if the hand is a straight, False, otherwise
    """
    for i in range(1, len(values)):
        if values[i] + 1 != values[i - 1]:
            return False

    return True


def is_four_of_a_kind(values):
    """
    Determines, if these values contain a four of a kind.
    :param values: values of a poker hand
    :return: True, if the hand contains a four of a kind, False, otherwise
    """
    if same_values(values[1:]) or same_values(values[:-1]):
        return True

    return False


def is_full_house(values):
    """
    Determines, if these values contain a full house.
    :param values: values of a poker hand
    :return: True, if the hand contains a full house, False, otherwise
    """
    if ((same_values(values[:3]) and same_values(values[3:])) or
            (same_values(values[:2]) and same_values(values[2:]))):
        return True

    return False


def is_three_of_a_kind(values):
    """
    Determines, if these values contain a three of a kind.
    :param values: values of a poker hand
    :return: True, if the hand contains a three of a kind, False, otherwise
    """
    if same_values(values[:3]) or same_values(values[1:4]) or same_values(values[-3:]):
        return True

    return False


def is_two_pairs(values):
    """
    Determines, if these values contain two pairs.
    :param values: values of a poker hand
    :return: True, if the hand contains two pairs, False, otherwise
    """
    if ((same_values(values[:2]) and (same_values(values[2:4]) or same_values(values[-2:]))) or
            (same_values(values[1:3]) and same_values(values[-2:]))):
        return True

    return False


def is_one_pair(values):
    """
    Determines, if these values contain a pair.
    :param values: values of a poker hand
    :return: True, if the hand contains a pair, False, otherwise
    """
    if (same_values(values[:2]) or same_values(values[1:3]) or
            same_values(values[2:4]) or same_values(values[-2:])):
        return True

    return False


def high_card(values):
    """
    Returns the high card value from list of values of a poker hand.
    :param values: values of a poker hand
    :return: high card value
    """
    # since the list of values is sorted in calling function,
    # the highest card is first in the list
    return values[0]


def higher_card(player1, player2):
    """
    Determines, if player 1 has high card over player 2.
    :param player1: values of a poker hand of player 1
    :param player2: values of a poker hand of player 2
    :return: True, if player 1 has high or equal card compared to player 2,
             False, otherwise
    """
    for i in range(len(player1)):
        if high_card(player1[i:]) > high_card(player2[i:]):
            return True
        elif high_card(player1[i:]) < high_card(player2[i:]):
            return False

    return True


def reorganize_values(values, hand_type=None):
    """
    Reorganize values of the values list so that paired cards would be the first.
    :param values: list of values
    :param hand_type: optional hand type (default=None)
    :return: reorganized list of values
    """
    if hand_type == 'FOK':
        # four of a kind first, then the remaining card
        # Y X X X X
        if values[0] != values[1]:
            # X X X X Y
            values[0], values[-1] = values[-1], values[0]
    elif hand_type == 'FH':
        # three of a kind first, then the pair
        # Y Y X X X
        if values[1] != values[2]:
            # X Y X Y X
            values[0], values[-2] = values[-2], values[0]
            # X X X Y Y
            values[1], values[-1] = values[-1], values[1]
    elif hand_type == 'TOK':
        # three of a kind first, then other cards in descending order
        # Y X X X Z
        # Y Z X X X
        if values[0] != values[1]:
            # X X X Y Z
            # X Z X Y X
            values[0], values[-2] = values[-2], values[0]
            # X Z X Y X
            if values[-1] == values[2]:
                # X X X Y Z
                values[1], values[-1] = values[-1], values[1]
    elif hand_type == 'TP':
        # two pairs in descending order first, then other card
        # 4 X X Y Y
        if values[0] != values[1]:
            # Y X X Y 4
            values[0], values[-1] = values[-1], values[0]
            # J 8 8 J 4
            if values[1] < values[-2]:
                # J J 8 8 4
                values[1], values[-2] = values[-2], values[1]
            # 8 J J 8 4
            else:
                # J J 8 8 4
                values[0], values[2] = values[2], values[0]
        else:
            # X X 4 Y Y
            if values[2] != values[-2]:
                # 8 8 4 J J
                if values[0] < values[-2]:
                    # 8 8 J J 4
                    values[2], values[-1] = values[-1], values[2]
                    # J 8 J 8 4
                    values[0], values[-2] = values[-2], values[0]
                    # J J 8 8 4
                    values[1], values[2] = values[2], values[1]
                # J J 4 8 8
                else:
                    # J J 8 8 4
                    values[2], values[-1] = values[-1], values[2]
            # X X Y Y 4
            else:
                # 8 8 J J 4
                if values[0] < values[2]:
                    # J 8 J 8 4
                    values[0], values[-2] = values[-2], values[0]
                    # J J 8 8 4
                    values[1], values[2] = values[2], values[1]
    elif hand_type == 'OP':
        # the pair first, then other cards in descending order
        if values[0] != values[1]:
            if values[1] != values[2]:
                # W Y Z X X
                if values[2] != values[3]:
                    # W X Z Y X
                    values[1], values[-2] = values[-2], values[1]
                    # W X X Y Z
                    values[2], values[-1] = values[-1], values[2]
                    # X X W Y Z
                    values[0], values[2] = values[2], values[0]
                # W Y X X Z
                else:
                    # X Y W X Z
                    values[0], values[2] = values[2], values[0]
                    # X X W Y Z
                    values[1], values[-2] = values[-2], values[1]
            # W X X Y Z
            else:
                # X X W Y Z
                values[0], values[2] = values[2], values[0]

    return values


def same_values(values):
    """
    Determines, if given list of values contains only one repeated value.
    :param values: a list of values
    :return: True, if values contain only one repeated value, False, otherwise
    """
    for i in range(1, len(values)):
        if values[0] != values[i]:
            return False

    return True


def value(val):
    """
    Return integer value of a poker card value.
    :param val: value of a poker card
    :return: integer value of val
    """
    if val.isnumeric():
        return int(val)
    else:
        if val == 'T':
            return 10

        if val == 'J':
            return 11

        if val == 'Q':
            return 12

        if val == 'K':
            return 13

        if val == 'A':
            return 14

        # wrong value entered
        return -1


player1_wins = 0
poker_hands = {'HC': 0, 'OP': 1, 'TP': 2, 'TOK': 3, 'S': 4, 'F': 5,
               'FH': 6, 'FOK': 7, 'SF': 8, 'RF': 9}

with open('../../res/p054_poker.txt', 'r') as f:
    line = f.readline()

    while line:
        if line[-1] == '\n':
            line = line[:-1]

        player1, player2 = parse_hands(line)

        if better_hand(player1, player2):
            player1_wins += 1

        line = f.readline()

print(player1_wins)
