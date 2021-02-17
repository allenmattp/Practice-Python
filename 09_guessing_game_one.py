"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
Keep the game going until the user types “exit”.
"""

import random

def main():
    # Track number of guesses
    guess = 0

    # Keep playing?
    quit = False

    # Number to guess
    computer = random.randrange(1, 10)
    while not quit:
        entry = input("Guess the number: ")
        guess += 1
        # check if user entered a number
        try:
            entry = int(entry)
            if entry == computer:
                print("You got it!"
                      "\nGuesses:", guess)
                quit = True
            # guess is high
            elif entry > computer:
                print("Oops, too high!")
            # player is low
            elif entry < computer:
                print("Oops, too low!")
            # player enters something else
        # per challenge instruction, only quit if they type exit
        except:
            if entry == "exit":
                quit = True
    print("Thanks for playing! Total guesses:", guess)

if __name__ == '__main__':
    main()