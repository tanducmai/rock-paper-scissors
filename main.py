#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =============================================================================
#
#        FILE:  main.py
#      AUTHOR:  Tan Duc Mai
#       EMAIL:  tan.duc.work@gmail.com
#     CREATED:  27-Nov-21
# DESCRIPTION:  Creates a rock-paper-scissors game.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#
# =============================================================================

# ------------------------------- Module Import -------------------------------
# Stdlib
import random

# Third party
import icontract


# ---------------------------- Function Definitions ---------------------------
@icontract.ensure(lambda result: result is None)
def display_details():
    """Display author's details.

    Returns
    -------
    None
    """
    print('Author: Tan Duc Mai',
          'Email: tan.duc.work@gmail.com',
          sep='\n',
          end='\n\n')


@icontract.ensure(lambda result: isinstance(result, int))
def generate_number():
    """Generate a random number in the range (1-3) inclusive."""
    return random.randint(1, 3)


@icontract.ensure(lambda result: isinstance(result, int))
def get_choice():
    """Prompt for, read, and validate user's guess.

    Returns
    -------
    int
        The valid guess received from the user.
    """
    choice = None

    while choice is None or choice not in range(1, 4):
        try:
            choice = float(input('Rock(1), Paper(2) or Scissors(3)? '))
            if choice not in range(1, 4):
                print('Error: number not in range\n')
        except ValueError as e:
            print('Error:', e, '\n')

    return int(choice)


@icontract.require(
    lambda player_1, player_2, count_win:
        isinstance(player_1, int) & isinstance(player_2, int)
        & isinstance(count_win, int))
@icontract.ensure(lambda result: isinstance(result, int))
def determine_winner(player_1, player_2, count_win):
    """Play the game of rock-paper-scissors.

    Parameters
    ----------
    player_1 : int
        An integer value that represents the user's choice.
    player_2 : int
        An integer value that represents the computer's choice.
    count_win : int
        The number of times the user won the game.

    Returns
    -------
    int
        The number of times the user won the game.
    """
    players = (player_1, player_2)
    win_pairs = ((1, 3), (2, 1), (3, 2))

    if players == players[::-1]:
        print('Draw - no winner!')
    else:
        if players in win_pairs:
            # winner = players[0]
            print('You win', end=' - ')
            count_win += 1
        else:
            # players[::-1] in win_pairs
            # winner = players[1]
            print('You lose', end=' - ')

        if win_pairs[0] in {players, players[::-1]}:
            print('rock crushes scissors!')
        elif win_pairs[1] in {players, players[::-1]}:
            print('paper covers rocks!')
        else:
            print('scissors cut paper!')

    return count_win


# ------------------------------- Main Function -------------------------------
def main():
    # Variable initialisation.
    selections = {
        1: 'rock',
        2: 'paper',
        3: 'scissors',
    }
    rounds = count_win = 0
    valid_answers = ('', 'y', 'yes', 'n', 'no')
    play = ''

    # Start looping the game.
    while play.lower() not in valid_answers[3:]:
        rounds += 1

        # Prompt for, read, and validate user's guess.
        user = get_choice()

        print('You chose', selections[user], end='.\n')

        # Computer's choice.
        comp = generate_number()

        print('Computer chose', selections[comp], end='.\n')

        # Start the game and determine the winner.
        # Return how many times the user won the game.
        count_win = determine_winner(user, comp, count_win)

        # Ask to play again.
        play = None

        while play not in valid_answers:
            play = input('\nDo you want to play again [Y/n]? ')
            if play.lower() not in valid_answers:
                print(f'Please answer one of {", ".join(valid_answers[1:])}.')

        print()

    # Summary.
    print('Game Summary',
          '------------',
          'You played ' + str(rounds) + ' games:',
          '* Won         : ' + str(count_win),
          '* Lost & Drew : ' + str(rounds - count_win),
          '* Percentage  : {:.2%}'.format(count_win/rounds),
          '\nThanks for playing!',
          sep='\n')


# --------------------------- Call the Main Function --------------------------
if __name__ == '__main__':
    main()
