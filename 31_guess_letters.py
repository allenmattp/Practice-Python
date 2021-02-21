"""
For this exercise, write the logic that asks a player to guess a letter and
displays letters in the clue word that were guessed correctly.
For now, let the player guess an infinite number of times until they get the entire word.
As a bonus, keep track of the letters the player guessed and
display a different message if the player tries to guess that letter again.
Remember to stop the game when all the letters have been guessed correctly!
Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining
"""
import random


def guess_letter(word):
    over = False                                            # is game over?
    guess = 0                                               # how many guesses?
    string = ["_" for l in word]                            # create string to show correct guesses
    guessed_letters = []                                    # create list to track guessed letters

    while not over:
        [print(l, end="") for l in string]                  # show current status of word
        letter = input("\nGuess a letter: ").upper()        # take user's guess
        letter = letter[0]                                  # only accept first letter

        if letter in guessed_letters:                       # check to see if letter has been guessed
            print("Whoops, you already guessed that.")

        elif letter in word:                                # letter is in word
            print("Correct!")
            for l in range(len(word)):
                if letter == word[l]:
                    string[l] = letter
            if "_" not in string:                           # check if solved
                [print(l, end="") for l in string]
                print("\nCongratulations! You got it!")
                over = True

        else:                                               # letter not in word
            guess += 1
            print("Incorrect.")
            if guess > 9:                                   # end if max guesses reached
                print("Sorry, you lose!")
                print("It was", word)
                over = True

        guessed_letters.append(letter)                      # track guessed letters
        print("Guessed letters:\n", guessed_letters, "\n")


def word_gen(file_name):                                    # select random word from file
    with open(file_name, "r") as file:
        words = file.read().splitlines()
        word = words[random.randrange(len(words))]
    file.close()
    return word


if __name__ == '__main__':
    file = "sowpods.txt"
    guess_letter(word_gen(file))