"""
Create a program that will play the “cows and bulls” game with the user.
"""

import random


def start():
    # user sets length of number to guess
    try:
        difficulty = int(input("Enter how many digits you want to try: "))
        return difficulty
    except ValueError:
        print("Whoops! Please choose the length of the number you wish to guess.")
        start()

def main(difficulty):
    # take in user's desired difficulty and convert to string for formatting
    # If user enters zero, set length to 4
    if not difficulty:
        print("OK, setting number length to default.")
        difficulty = 4
    length = str(difficulty)
    # generate random number user will need to guess
    # make sure that user didn't enter a negative length
    try:
        number = f'{random.randrange(10**difficulty):{length}}'
    except ValueError:
        print("Did you enter a negative number?")
        main(start())
    # track attempts
    attempt = 0
    # game will run until user guess correctly
    correct = False

    while not correct:
        # game variables
        cow = 0
        bull = 0
        guess = str(input("Enter a number: "))
        # compare user's input versus computer's number
        # warn user if they enter a weird length
        try:
            for i in range(difficulty):
                if guess[i] == number[i]:
                    cow += 1
                else:
                    bull += 1
        except IndexError:
            print("Make sure to only enter a", difficulty, "digit number")
        print("Cows: ", cow, "Bulls: ", bull)
        attempt += 1
        if cow == len(number):
            correct = True
    print("That's it! Thanks for playing!")
    print("Total guesses: ", attempt)


if __name__ == '__main__':
    print("Welcome to the Cows and Bulls game!\n")
    main(start())
