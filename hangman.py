"""
Hangman
Author: Connor Shoen
Based on: Al Sweigart from The Big Book of Small Python Projects
"""

# Imports
import random, sys

# ASCII Graphics
HANGMAN_PICS = [r"""
   _________
   |       |
   |
   |
   |
   |
___|___

""",r"""
   _________
   |       |
   |       O
   |
   |
   |
___|___

""",r"""
   _________
   |       |
   |       O
   |       |
   |
   |
___|___

""",r"""
   _________
   |       |
   |       O
   |     / |
   |
   |
___|___

""",r"""
   _________
   |       |
   |       O
   |      /|\
   |       |
   |      /
___|___

""",r"""
   _________
   |       |
   |       O
   |      /|\
   |       |
   |      / \
___|___

"""]

# Categories and Words section
CATEGORY = 'Animals'

WORDS = 'ANT BADGER BEAVER DONKEY EAGLE GOOSE LIZARD MONKEY MOUSE PARROT PYTHON RABBIT SHARK SPIDER TURTLE WEASLE WOMBAT'.split()

# Main Program
def main():
    print ("Hangman, By: Connor Shoen")
    print ("=============================================================\n")
    print ("Based on Al Sweigart's The Big Book of Small Python Projects\n\n")

    # Setup variable for a new game
    missed_letters = [] # List of wrong guessed letters
    correct_letters = [] # List of right letters guessed
    secret_word = random.choice(WORDS)

# Draw current state of hangman game along with missed and correctly guessed letters of the secret word
def draw_hm(missed_letters, correct_letters, secret_word):
    print (HANGMAM_PICS[len(missed_letters)])
    print ('The category selected is: ' + CATEGORY)
    print ()

    # Incorrectly guessed letters
    blanks = ['_'] * len(secret_word)

    #  Display blanks for the secret word


    # Replace blanks with correct letters
    

    # Show the secret word with spaces in between each letter


    # Returns letter player entered. Makes sure single letter was entered they haven't guessed before.


# If this program was run (instead of imported), run the game
if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        sys.exit() # When someone hits Ctrl-C, ends program