board = [""] * 9
line = '-' * 11
win = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
def gameboard():
    for i in range(len(board)):
        if (i + 1) % 3 == 0:
            print("%3s" % (board[i]))
        else:
            print("%3s|" % (board[i]), end="")
        if (i + 1) % 3 == 0 and (i + 1) != len(board):
            print("%3s" % line)
def setplayerchoice(symbol):
    choice = int(input("enter a choise of number  for player (1 to 9) :  "))
    while not (choice < 10 and choice > 0):
        choice = int(input("enter a choise of number  for player (1 to 9) :  "))
    if board[choice - 1] == '':
        board[choice - 1] = symbol
    else:
        setplayerchoice(symbol)
def check_win(player_choice):
    win1 = False
    for i in win:
        for z in i:
            if board[z] == player_choice:
                win1 = True
            else:
                win1 = False
                break
        if win1:
            break
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
    for i in range(1, 10):
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
print("\t\t\t\t\twel-come tic tac game")
print("\t\t\t\t  -------------------------")
gameplay()
