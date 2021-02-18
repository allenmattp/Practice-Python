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
        print("Whoops! Please enter a number for the length of the code you wish to guess.")
        start()


def number_gen(n):
    # Generate number that is n-digits long that are all unique
    # Create set of numbers 0-9
    num_list = [x for x in range(10)]
    # Set length to 4 if user enters invalid length
    if n < 1 or n > 10:
        print("Invalid range, setting number length to default.")
        n = 4
    # shuffle set to create a random number
    random.shuffle(num_list)
    number = ''.join([str(num_list[i]) for i in range(n)])
    return number


def main(number):

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
            for i in range(len(number)):
                if guess[i] == number[i]:
                    bull += 1
                elif guess[i] in number and guess[i] != number[i]:
                    cow += 1
        except IndexError:
            print("Make sure to only enter a", len(number), "digit number")
        print("Cows: ", cow, "Bulls: ", bull)
        attempt += 1
        if bull == len(number):
            correct = True
    print("That's it! Thanks for playing!")
    print("Total guesses: ", attempt)


if __name__ == '__main__':
    print("Welcome to the Cows and Bulls game!\n")
    main(number_gen(start()))
