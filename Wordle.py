# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
Update this comment to describe the final implementation once completed.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    # create a WordleGWindow instance
    gw = WordleGWindow()

    # pick a random word from the list of five-letter words
    solution_word = random.choice(FIVE_LETTER_WORDS).upper()

    # this function will be called when the user hits ENTER
    def enter_action(s):
        # convert the entered word to uppercase for comparison
        entered_word = s.lower()

        # check if the entered word is in the list of five-letter words
        if entered_word in FIVE_LETTER_WORDS:
            # for now, just show a positive message (this will be updated in later milestones)
            gw.show_message("That's a valid word!")
        else:
            # show a message that the word is not in the list
            gw.show_message("Not in word list")

    # add the enter listener (enter_action)
    gw.add_enter_listener(enter_action)

    # Note: The following code is commented out as it was only needed for Milestone #1
    # Displaying the solution word is not needed for Milestone #2 or actual gameplay
    # for col in range(N_COLS):
    #     gw.set_square_letter(0, col, solution_word[col])


# Startup code
if __name__ == "__main__":
    wordle()
