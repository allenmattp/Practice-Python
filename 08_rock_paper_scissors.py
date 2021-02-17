"""
Make a two-player RPS game.
"""

import random

def main():
    # Track record
    win = 0
    loss = 0
    draw = 0

    # Keep playing?
    quit = False

    while not quit:
        entry = str(input("Rock, Paper, or Scissors? "))
        # rock = 0, paper = 1, scissors = 2
        computer = random.randrange(3)
        # Player chooses rock
        if entry[0].lower() == "r":
            if not computer:
                draw += 1
                print("Rock vs rock! It's a draw.")
            elif computer == 1:
                loss += 1
                print("Paper beats rock! You lose.")
            else:
                win += 1
                print("Rock beats scissors! You win.")
        # player chooses paper
        elif entry[0].lower() == "p":
            if not computer:
                win += 1
                print("Paper beats rock! You win")
            elif computer == 1:
                draw += 1
                print("Paper vs paper! It's a draw.")
            else:
                loss += 1
                print("Scissors beat paper! You lose.")
        # player chooses scissors
        elif entry[0].lower() == "s":
            if not computer:
                loss += 1
                print("Rock beats scissors! You lose")
            elif computer == 1:
                win += 1
                print("Scissors beat paper! You win.")
            else:
                draw += 1
                print("Scissors vs scissors! It's a draw.")
        # player enters something else
        else:
            print("Hmm, I don't recognize that.")
        reply = str(input("Play again? "))
        if reply[0].lower() == "n":
            quit = True

    print("Thanks for playing! Your final score:")
    print("Wins:", win, "Losses:", loss, "Draws:", draw)
    print("Win pct:", ((win / (win + loss + draw))))


if __name__ == "__main__":
    main()