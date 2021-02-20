"""
Given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any.
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
"""


def check(game):
    check = []
    # rows
    for i in range(3):
        check.clear()
        for j in range(3):
            check.append(game[i][j])
        # if row value is non-zero and only one value found in set, declare winner
        if check[0] and len(set(check)) == 1:
            print("winner!", check[0])

    # columns
    for i in range(3):
        check.clear()
        for j in range(3):
            check.append(game[j][i])
        # if column value is non-zero and only one value found in set, declare winner
        if check[0] and len(set(check)) == 1:
            print("winner!", check[0])

    # check if diagonal values are non-zero and match
    if game[1][1] and ((game[0][0] == game[1][1] and game[1][1] == game[2][2]) or (game[0][2] == game[1][1] and game[1][1] == game[2][0])):
        print("winner!", game[1][1])


if __name__ == '__main__':
    winner_is_2 = [[2, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

    no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]

    print("winner is 2:")
    check(winner_is_2)
    print("winner is 1:")
    check(winner_is_1)
    print("winner is also 1:")
    check(winner_is_also_1)
    print("no winner:")
    check(no_winner)
    print("no winner:")
    check(also_no_winner)