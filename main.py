#!/usr/bin/python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         27-Nov-21
# Description:  Creates a rock-paper-scissors game.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ------------------------------- Module Import -------------------------------
import random


# ------------------------------- Named Constant ------------------------------
SELECTION = ['rock', 'paper', 'scissors']


# ---------------------------- Function Definitions ---------------------------
def display_details():
    print(
        'Author: Tan Duc Mai',
        'Email: tan.duc.work@gmail.com',
        sep='\n',
        end='\n\n',
    )


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


def rock_paper_sci(player_1, player_2, win):
    """Play the game of rock-paper-scissors.

    Parameters
    ----------
    player_1 : int
        An integer value that represents the user's choice.
    player_2 : int
        An integer value that represents the computer's choice.
    win : int
        The number of times the user won the game.

    Returns
    -------
    int
        The number of times the user won the game.
    """
    PLAYERS = [player_1, player_2]
    win_pairs = [
            ['rock', 'scissors'],
            ['paper', 'rock'],
            ['scissors', 'paper'],
    ]

    if PLAYERS == PLAYERS[::-1]:
        print('Draw - no winner!')
    else:
        if PLAYERS in win_pairs:
            # winner = PLAYERS[0]
            print('You win', end=' - ')
            win += 1
        else:
            # PLAYERS[::-1] in win_pairs
            # winner = PLAYERS[1]
            print('You lose', end=' - ')

        if (PLAYERS == win_pairs[0]
                or PLAYERS[::-1] == win_pairs[0]):
            print('rock crushes scissors!')
        elif (PLAYERS == win_pairs[1]
                or PLAYERS[::-1] == win_pairs[1]):
            print('paper covers rocks!')
        else:
            print('scissors cut paper!')

    return win


# ------------------------------- Main Function -------------------------------
def main():
    # Variable initialisation.
    rounds = 0
    count_win = 0
    play = 'y'
    valid_answers = ['y', 'yes', 'n', 'no']

    while play not in valid_answers[2:4]:
        rounds += 1

        # Prompt for, read, and validate user's guess.
        user = get_choice()

        print('You chose', SELECTION[user - 1], end='.\n')

        # Computer's choice.
        comp = random.randint(1, 3)

        print('Computer chose', SELECTION[comp - 1], end='.\n')

        # Start the game and determine the winner.
        # Return how many times the user won the game.
        count_win = rock_paper_sci(user, comp, count_win)

        # Ask to play again.
        play = input('\nDo you want to play again [Y/n]? ')

        while play.lower() not in valid_answers:
            print(f"Please answer one of {', '.join(valid_answers)}.")
            play = input('\nDo you want to play again [Y/n]? ')

        play = play.lower()
        print()

    # Summary.
    print(
        f'\nGame Summary',
        f'------------',
        f'You played {rounds} games:',
        f'* Won:          {count_win}',
        f'* Lost & Drew:  {rounds - count_win}',
        f'\nThanks for playing!',
        sep='\n',
    )


# --------------------------- Call the Main Function --------------------------
if __name__ == '__main__':
    main()
