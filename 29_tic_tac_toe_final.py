"""
Your challenge in this exercise is to use the functions from those previous exercises
all together in the same program to make a two-player game that you can play with a friend.

ASCII text generated using https://patorjk.com/software/taag/
"""


def main():
    print("""
        ,----,                                  ,----,                                   ,----,                   
      ,/   .`|                                ,/   .`|                                 ,/   .`|                   
    ,`   .'  :                              ,`   .'  :                               ,`   .'  :                   
  ;    ;     / ,--,                       ;    ;     /                             ;    ;     /                   
.'___,/    ,',--.'|                     .'___,/    ,'                            .'___,/    ,'  ,---.             
|    :     | |  |,                      |    :     |                             |    :     |  '   ,'\            
;    |.';  ; `--'_       ,---.          ;    |.';  ;  ,--.--.     ,---.          ;    |.';  ; /   /   |   ,---.   
`----'  |  | ,' ,'|     /     \         `----'  |  | /       \   /     \         `----'  |  |.   ; ,. :  /     \  
    '   :  ; '  | |    /    / '             '   :  ;.--.  .-. | /    / '             '   :  ;'   | |: : /    /  | 
    |   |  ' |  | :   .    ' /              |   |  ' \__\/: . ..    ' /              |   |  ''   | .; :.    ' / | 
    '   :  | '  : |__ '   ; :__             '   :  | ," .--.; |'   ; :__             '   :  ||   :    |'   ;   /| 
    ;   |.'  |  | '.'|'   | '.'|            ;   |.' /  /  ,.  |'   | '.'|            ;   |.'  \   \  / '   |  / | 
    '---'    ;  :    ;|   :    :            '---'  ;  :   .'   \   :    :            '---'     `----'  |   :    | 
             |  ,   /  \   \  /                    |  ,     .-./\   \  /                                \   \  /  
              ---`-'    `----'                      `--`---'     `----'                                  `----'   
                                                                                                                 
    """)                                        # generated using https://patorjk.com/software/taag/

    print("\nWelcome to Tic-Tac-Toe!\n\n"       # introduce game 
          "Enter your move as a row, column coordinate.\n"
          "For example, the middle square is 2, 2.\n"
          "The bottom-left corner would be 3, 1.\n"
          "Good luck, have fun!")
    score_one = 0                              # start with no score
    score_two = 0
    game_logic(score_one, score_two)


def game_logic(score_one, score_two):           # track player scores
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
    if score_one > score_two:                   # The Player with the lower score goes first
        turn = 1
    else:                                       # Player 1 goes first if tied or first game
        turn = 0

    while not winner:
        game_board = player_move(game_board, turn)
        turn += 1
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
        winner = check_for_winner(game_board)
        if turn >= 9 and not winner:
            winner = "cat"
    declare_winner(winner, score_one, score_two)


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
                print("PLAYER 1")
                move = 1
            elif not player_turn:
                print("PLAYER 2")
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


def check_for_winner(game):
    check = []
    for i in range(3):                          # check rows for a winner
        check.clear()
        for j in range(3):
            check.append(game[i][j])
        # if row value is non-zero and only one value found in set, declare winner
        if check[0] and len(set(check)) == 1:
            return check[0]

    for i in range(3):                          # check columns for a winner
        check.clear()
        for j in range(3):
            check.append(game[j][i])
        # if column value is non-zero and only one value found in set, declare winner
        if check[0] and len(set(check)) == 1:
            return check[0]

    # check if diagonal values are non-zero and match
    if game[1][1] and ((game[0][0] == game[1][1] and game[1][1] == game[2][2]) or (game[0][2] == game[1][1] and game[1][1] == game[2][0])):
        return game[1][1]


def score(winner, score_one, score_two):
    if winner == 1:
        score_one += 1
    elif winner == 2:
        score_two += 1
    print("Current Score:")
    print("Player 1:", score_one)
    print("Player 2:", score_two)
    again = str(input("Play again? ")).lower()
    if "y" in again:
        game_logic(score_one, score_two)
    else:
        print("Thank you for playing!")
        print("""
                                                                         ,`--.' |  
  ,----..                                                                |   :  :  
 /   /   \                            ,---,  ,---,                       '   '  ;  
|   :     :    ,---.     ,---.      ,---.'|,---.'|                       |   |  |  
.   |  ;. /   '   ,'\   '   ,'\     |   | :|   | :                       '   :  ;  
.   ; /--`   /   /   | /   /   |    |   | |:   : :         .--,   ,---.  |   |  '  
;   | ;  __ .   ; ,. :.   ; ,. :  ,--.__| |:     |,-.    /_ ./|  /     \ '   :  |  
|   : |.' .''   | |: :'   | |: : /   ,'   ||   : '  | , ' , ' : /    /  |;   |  ;  
.   | '_.' :'   | .; :'   | .; :.   '  /  ||   |  / :/___/ \: |.    ' / |`---'. |  
'   ; : \  ||   :    ||   :    |'   ; |:  |'   : |: | .  \  ' |'   ;   /| `--..`;  
'   | '/  .' \   \  /  \   \  / |   | '/  '|   | '/ :  \  ;   :'   |  / |.--,_     
|   :    /    `----'    `----'  |   :    :||   :    |   \  \  ;|   :    ||    |`.  
 \   \ .'                        \   \  /  /    \  /     :  \  \\   \  / `-- -`, ; 
  `---`                           `----'   `-'----'       \  ' ; `----'    '---`"  
                                                           `--`                    
        """)


def declare_winner(winner, score_one, score_two):
    win = """
                                 ,--.             
           .---.   ,---,       ,--.'|  .--.--.    
          /. ./|,`--.' |   ,--,:  : | /  /    '.  
      .--'.  ' ;|   :  :,`--.'`|  ' :|  :  /`. /  
     /__./ \ : |:   |  '|   :  :  | |;  |  |--`   
 .--'.  '   \' .|   :  |:   |   \ | :|  :  ;_     
/___/ \ |    ' ''   '  ;|   : '  '; | \  \    `.  
;   \  \;      :|   |  |'   ' ;.    ;  `----.   \ 
 \   ;  `      |'   :  ;|   | | \   |  __ \  \  | 
  .   \    .\  ;|   |  ''   : |  ; .' /  /`--'  / 
   \   \   ' \ |'   :  ||   | '`--'  '--'.     /  
    :   '  |--" ;   |.' '   : |        `--'---'   
     \   \ ;    '---'   ;   |.'                   
      '---"             '---'                    
    """
    if winner == 1:
        print("""
,-.----.                                                                       
\    /  \    ,--,                                                        ,---, 
|   :    \ ,--.'|                                                     ,`--.' | 
|   |  .\ :|  | :                                    __  ,-.         /    /  : 
.   :  |: |:  : '                                  ,' ,'/ /|        :    |.' ' 
|   |   \ :|  ' |     ,--.--.        .--,   ,---.  '  | |' |        `----':  | 
|   : .   /'  | |    /       \     /_ ./|  /     \ |  |   ,'           '   ' ; 
;   | |`-' |  | :   .--.  .-. | , ' , ' : /    /  |'  :  /             |   | | 
|   | ;    '  : |__  \__\/: . ./___/ \: |.    ' / ||  | '              '   : ; 
:   ' |    |  | '.'| ," .--.; | .  \  ' |'   ;   /|;  : |              |   | ' 
:   : :    ;  :    ;/  /  ,.  |  \  ;   :'   |  / ||  , ;              '   : | 
|   | :    |  ,   /;  :   .'   \  \  \  ;|   :    | ---'               ;   |.' 
`---'.|     ---`-' |  ,     .-./   :  \  \\   \  /                     '---'   
  `---`             `--`---'        \  ' ; `----'                              
                                     `--`                                      
        """)
        print(win)
        score(winner, score_one, score_two)
    elif winner == 2:
        print("""
,-.----.                                                                           
\    /  \    ,--,                                                         ,----,   
|   :    \ ,--.'|                                                       .'   .' \  
|   |  .\ :|  | :                                    __  ,-.          ,----,'    | 
.   :  |: |:  : '                                  ,' ,'/ /|          |    :  .  ; 
|   |   \ :|  ' |     ,--.--.        .--,   ,---.  '  | |' |          ;    |.'  /  
|   : .   /'  | |    /       \     /_ ./|  /     \ |  |   ,'          `----'/  ;   
;   | |`-' |  | :   .--.  .-. | , ' , ' : /    /  |'  :  /              /  ;  /    
|   | ;    '  : |__  \__\/: . ./___/ \: |.    ' / ||  | '              ;  /  /-,   
:   ' |    |  | '.'| ," .--.; | .  \  ' |'   ;   /|;  : |             /  /  /.`|   
:   : :    ;  :    ;/  /  ,.  |  \  ;   :'   |  / ||  , ;           ./__;      :   
|   | :    |  ,   /;  :   .'   \  \  \  ;|   :    | ---'            |   :    .'    
`---'.|     ---`-' |  ,     .-./   :  \  \\   \  /                  ;   | .'       
  `---`             `--`---'        \  ' ; `----'                   `---'          
                                     `--`                                           
        """)
        print(win)
        score(winner, score_one, score_two)
    else:
        print("""
          ,.                 .,
         ,: ':.    .,.    .:' :,
         ,',   '.:'   ':.'   ,',
         : '.  '         '  .' :
         ', : '           ' : ,'
         '.' .,:,.   .,:,. '.'
          ,:    V '. .' V    :,
         ,:        / '        :,
         ,:                   :,
          ,:       =:=       :,
           ,: ,     :     , :,
            :' ',.,' ',.,:' ':
           :'      ':WW::'   '.
          .:'       '::::'   ':
          ,:        '::::'    :,
          :'         ':::'    ':
         ,:           ':''     :.
        .:'             '.     ',.
       ,:'               ''     '.
       .:'               .',    ':
      .:'               .'.,     :
      .:                .,''     :
      ::                .,''    ,:
      ::              .,'','   .:'
    .,::'.           .,','     ::::.
  .:'     ',.       ,:,       ,WWWWW,
  :'        :       :W:'     :WWWWWWW,          .,.
  :         ',      WWW      WWWWWWWWW          '::,
  '.         ',     WWW     :WWWWWWWWW            '::,
   '.         :     WWW     :WWWWWWWW'             :::
    '.       ,:     WWW     :WWWWWWW'             .:::
     '.     .W:     WWW     :WWWWWW'           .,:::'
      '.   :WW:     WWW     :WWWWW'      .,,:::::''
     .,'   ''::     :W:     :WWWWW.  .,::::''
  ,'        ''','',',','','''WWWWW::::''
   ':,,,,,,,':  :  : : :  :  :WWWW'''
    """)                                        # Found here: https://textart.io/art/tag/cat/1
        print("Cat's game!")
        score(winner, score_one, score_two)


if __name__ == '__main__':\
    main()