# we will run a simulation of 1 000 000 rounds of the game
# and that should give us the right first three squares
from random import randint


def simulate_n_rounds(n):
    """
    Runs simulation of n Monopoly rounds with two 4-sided dices.
    :param n: number of rounds
    :return: list of numbers denoting how many times we visited every square
    """
    current_pos = 0
    community_pos = 0
    chance_pos = 0
    doubles = 0
    squares = [0] * 40

    for _ in range(n):
        first_dice = randint(1, 4)
        second_dice = randint(1, 4)

        # checking for doubles
        if first_dice == second_dice:
            doubles += 1
        else:
            doubles = 0

        # three consecutive doubles -> go to JAIL
        if doubles == 3:
            # go to JAIL
            current_pos = 10
        else:
            # move
            current_pos = (current_pos + first_dice + second_dice) % 40

            # chance cards
            if current_pos == 7 or current_pos == 22 or current_pos == 36:
                # GO, JAIL, C1, E3, H2, R1
                chance = [0, 10, 11, 24, 39, 5]
                # take top card from chance pile
                chance_pos = (chance_pos + 1) % 16

                # we are only interested in the cards, that involve movement
                # first six cards (advance to GO, go to JAIL, C1, E3, H2, R1)
                if chance_pos < 6:
                    current_pos = chance[chance_pos]
                # go to next railway
                elif chance_pos == 6 or chance_pos == 7:
                    if current_pos == 7:
                        current_pos = 15
                    elif current_pos == 22:
                        current_pos = 25
                    elif current_pos == 36:
                        current_pos = 5
                # go to next utility
                elif chance_pos == 8:
                    if current_pos == 22:
                        current_pos = 28
                    else:
                        current_pos = 12
                # move back three squares
                elif chance_pos == 9:
                    current_pos -= 3

            # community cards
            if current_pos == 2 or current_pos == 17 or current_pos == 33:
                # GO, JAIL
                community = [0, 10]
                # take top card from community pile
                community_pos = (community_pos + 1) % 16

                # we are only interested in the cards, that involve movement
                if community_pos < 2:
                    current_pos = community[community_pos]

            # go to JAIL
            if current_pos == 30:
                current_pos = 10

        # if went to JAIL, doubles are reset
        if current_pos == 10:
            doubles = 0

        squares[current_pos] += 1

    return squares


squares = simulate_n_rounds(1000000)
squares = sorted([(i, squares[i]) for i in range(len(squares))], key=lambda i: i[1], reverse=True)
print(''.join([str(i[0]) for i in squares[:3]]))
