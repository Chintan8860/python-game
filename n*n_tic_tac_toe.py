from math import sqrt
def set_matrix(n=3):
    return n
n=set_matrix(5)

board = [""] * pow(n,2)
gboard_len=int(sqrt(len(board)))
line = '-' * pow(n,2)

def gameboard():
    for i in range(len(board)):
        if (i + 1) % n == 0:
            print("%3s" % (board[i]))
        else:
            print("%3s|" % (board[i]), end="")
        if (i + 1) % n == 0 and (i + 1) != len(board):
            print("%3s" % line)
def setplayerchoice(symbol):
    choice = int(input("enter a choise of number  for player  : (1 to %d) "% (len(board))))
    while not (choice < pow(n,2)+1 and choice > 0):
        choice = int(input("enter a choise of number  for player  :(1 to %d)"%(len(board))))
    if board[choice - 1] == '':
        board[choice - 1] = symbol
    else:
        setplayerchoice(symbol)
def check_win( play_choise ):
    win1 = False
    for i in range(gboard_len):
        if board[i:len(board):n].count(play_choise) == n:
            if play_choise == '0':
                print("SYMBOL 0 win with COLUMAN")
                win1 = True
            else:
                print("SYMBOL X win WITH COLUMAN")
                win1 = True
        if board[i:gboard_len].count(play_choise) == n:
            if play_choise == '0':
                print("SYMBOL 0 win with ROW")
                win1 = True
            else:
                print("SYMBOL X win ROW")
                win1 = True
        if board[0:len(board):gboard_len + 1].count(play_choise) == n:
            if play_choise == '0':
                print("SYMBOL 0 win with right diagonal")
                win1 = True
            else:
                print("SYMBOL X win right diagonal")
                win1 = True
        if board[gboard_len - 1:len(board):gboard_len - 1].count(play_choise) == n:
            if play_choise == '0':
                print("SYMBOL 0 win with left diagonal")
                win1 = True
            else:
                print("SYMBOL X win left diagonal")
                win1 = True
    return win1
def gameplay():
    p1 = input("enter a player 1 choise 'X' or '0' : ")
    p2 = input("enter a player 2 choise 'X' or '0' : ")
    player1_choise = p1.upper()
    player2_choise = p2.upper()
    if player1_choise == '' and player2_choise == '':
        player1_choise = 'X'
        player2_choise = '0'
    elif player1_choise == '':
        if player2_choise == 'X':
            player1_choise = '0'
        elif player2_choise == '0':
            player1_choise = 'X'
    elif player2_choise == '':
        if player1_choise == 'X':
            player2_choise = '0'
        elif player1_choise == '0':
            player2_choise = 'X'
    print("player 1 choise selected is : ",player1_choise)
    print("player 2 choise selected is : ",player2_choise)
    for i in range(1, pow(n,2)+1):
        if check_win(player1_choise):
            print("Player 1 won")
            break
        elif check_win(player2_choise):
            print("Player 2 won")
            break
        else:
            if i % 2 != 0:
                setplayerchoice(player1_choise)
            else:
                setplayerchoice(player2_choise)
        gameboard()

gameplay()
