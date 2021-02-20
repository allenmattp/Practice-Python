"""
Exercise 27: Tic Tac Toe Draw
Store information about a tic tac toe game.
Approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.
Assume user thinks grid coordinates start as (1, 1) rather than (0, 0)
*** Don't implement Game logic (ie track when game is over) yet ***
"""


def turn_check(num):
    if not num % 2:                             # player x is even
        return True
    else:                                       # player o is odd
        return False


def player_move(game_board, turn):
    while True:
        try:
            move = ""
            player_turn = turn_check(turn)      # determine whose turn it is
            if player_turn:
                print("PLAYER X")
                move = 1
            elif not player_turn:
                print("PLAYER O")
                move = 2
            coord = input("Enter your move as row, col coordinates: ").split(",")
            row = int(coord[0]) - 1
            col = int(coord[1]) - 1
            if not game_board[row][col]:        # make sure the coordinates are empty
                game_board[row][col] = move
            else:                               # otherwise reject and ask again
                print("Invalid move. Choose a different space.")
                player_move(game_board, turn)
            return game_board
        except IndexError:                      # number entered is outside of grid
            print("Invalid coordinates. Enter number between 1-3.")
        except ValueError:                      # user doesn't type a number
            print("Invalid input. Please use numbers (e.g. 2, 2).")


def main():
    game_board = [                              # new game board
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    hori   = " ---"                             # game "graphics"
    vert   = "|   "
    vert_x = "| X "
    vert_o = "| O "

    winner = False                              # keep playing until winner declared
    turn = 0                                    # track whose turn it is

    while not winner:
        game_board = player_move(game_board, turn)
        turn += 1
        if turn == 9:                            # end game if no more spaces
            print("CAT'S GAME!")
            winner = True
        for i in range(3):                       # print 3x3 board
            print(hori * 3)
            for j in range(3):
                if game_board[i][j] == 1:
                    print(vert_x, end="")
                elif game_board[i][j] == 2:
                    print(vert_o, end="")
                else:
                    print(vert, end="")
            print(vert)
        print(hori * 3)


if __name__ == '__main__':
    main()