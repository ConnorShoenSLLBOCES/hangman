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
    print ("\n\nHangman, By: Connor Shoen")
    print ("=============================================================\n")
    print ("Based on Al Sweigart's The Big Book of Small Python Projects\n\n")

    # Setup variable for a new game
    missed_letters = [] # List of wrong guessed letters
    correct_letters = [] # List of right letters guessed
    secret_word = random.choice(WORDS)

    while True:
        draw_hm(missed_letters, correct_letters, secret_word)

        # Let the player enter guess
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            # Add correct guess to correct_letters
            correct_letters.append(guess)

         # Check if won
        found_all = True # start assuming user won
        for secret_letter in secret_word:
            if secret_letter not in correct_letters:
                found_all = False
                break
        if found_all:
            print (f'Yes, the secret word was: "{secret_word}"')
            print ("Victory is your's!")
            break
        else:
            # player has guessed incorrectly
            missed_letters.append(guess)

            # Check if player guessed wrong too many times the -1 is because we don't count empty gallows
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                draw_hm(missed_letters, correct_letters, secret_word)
                print ("\nYou have failed to guess correctly in the alloted 6 wrong guesses.")
                print (f'The word was "{secret_word}"' .format(secret_word))
                break

# Draw current state of hangman game along with missed and correctly guessed letters of the secret word
def draw_hm(missed_letters, correct_letters, secret_word):
    print (HANGMAN_PICS[len(missed_letters)])
    print ('The category selected is: ' + CATEGORY)
    print ()


    # Incorrectly guessed letters
    print ("Misssed letters:", end='')
    for letter in missed_letters:
        print (letter, end=' ')
    if len(missed_letters) == 0:
        print ("No missed letters... Yet. \n")

    #  Display blanks for the secret word
    blanks = ['_'] * len(secret_word)

    # Replace blanks with correct letters
    

    # Show the secret word with spaces in between each letter


    # Returns letter player entered. Makes sure single letter was entered they haven't guessed before.
def get_guess(already_guessed):
    while True: # keep asking until entered a valid letter
        print ("Guess a letter: ")
        guess = input ("> ").upper()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print ("You already guessed this letter. Choose again.")
        elif not guess.isalpha():
            print ("Please enter a letter.")
        else:
            return guess


# If this program was run (instead of imported), run the game
if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        sys.exit() # When someone hits Ctrl-C, ends program