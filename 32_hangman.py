#! python3
"""
In this exercise, we will finish building Hangman.
In the game of Hangman, the player only has 6 incorrect guesses
(head, body, 2 legs, and 2 arms) before they lose the game.
"""
import random
import hangman_art

streak = 0
high_score = 0

def guess_letter(word):
    over = False                                            # is game over?
    global streak                                           # current streak
    global high_score                                       # current high score
    guess = 0                                               # how many guesses?
    string = ["_" for l in word]                            # create string to show correct guesses
    guessed_letters = []                                    # create list to track guessed letters

    hangman_art.ascii(0)                                    # print welcome text
    hangman_art.hangmanpics(guess)                          # print starting

    while not over:
        if guess or string != list("_" * len(word)):        # don't print guessed letters first turn
            print("\nGuessed letters:\n", guessed_letters, "\n") # statement here
        [print(l, end=" ") for l in string]                 # show current status of word
        letter = input("\n\nGuess a letter: ").upper()      # take user's guess
        letter = letter[0]                                  # only accept first letter

        if letter in guessed_letters:                       # check to see if letter has been guessed
            print("Whoops, you already guessed that.")

        elif letter in word:                                # letter is in word
            print("")
            hangman_art.hangmanpics(guess)                  # print current gallows
            hangman_art.ascii(6)                            # print correct
            for l in range(len(word)):
                if letter == word[l]:
                    string[l] = letter
            if "_" not in string:                           # check if solved
                streak += 1
                [print(l, end=" ") for l in string]
                hangman_art.ascii(1)                        # print winning
                print("Current streak: ", streak)
                if streak > high_score:
                    high_score = streak
                print("High Score: ", high_score)
                over = True

        else:                                               # letter not in word
            print("")
            guess += 1
            hangman_art.hangmanpics(guess)                  # print current gallows
            hangman_art.ascii(5)                            # print incorrect
            if guess > 5:                                   # end if max guesses reached
                streak = 0
                if streak > high_score:
                    high_score = streak
                hangman_art.ascii(2)                        # print losing text
                print("It was", word)
                print("High Score: ", high_score)
                over = True
        if letter not in guessed_letters:
            guessed_letters.append(letter)                  # track guessed letters

    play_again()


def word_gen(file_name):                                    # select random word from file
    with open(file_name, "r") as file:
        words = file.read().splitlines()
        word = words[random.randrange(len(words))]
    file.close()
    return word


def play_again():
    again = str(input("Play again? ")).lower()
    if "y" in again:
        guess_letter(word_gen(file))
    else:
        hangman_art.ascii(3)



if __name__ == '__main__':
    file = "sowpods.txt"
    guess_letter(word_gen(file))