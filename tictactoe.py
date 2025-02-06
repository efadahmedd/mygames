
import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
playerchoice = "x"
winner = None
run = True


def printboard(board):
    print("-------------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("-------------")

def playerinput(board):
    while True:
        inp = int(input("give me your fav num between int(1-9) :"))
        if inp >=1 and inp <=9 and board[inp-1] == "-":
            board[inp-1] = playerchoice
            break
        else:
            if playerchoice=="x":
                print("cannot use a field twice")
            else:
                 
                print()
                print("pagol nki tumi!")


def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] == board[0] != "-":
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] == board[3] != "-":
        winner = board[3]
        return True
    
    elif board[6] == board[7] == board[8] == board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] == board[0] != "-":
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[7] == board[1] != "-":
        winner = board[1]
        return True
    
    elif board[2] == board[5] == board[8] == board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] == board[0] != "-":
        winner = board[0]
        return True
    
    elif board[2] == board[4] == board[6] == board[2] != "-":
        winner = board[2]
        return True


def checktie(board):
    global run
    if "-" not in board:
        printboard(board)
        print("it is a tie")
        run = False

def checkwin():
    global run
    if checkDiag(board) or checkHorizontle(board) or checkRow(board) :
        print(f"the winner is {winner}")
        run = False

def switchplayer():
    global playerchoice
    if playerchoice == "x" :
        playerchoice = "o"
    else:
        playerchoice = "x"

def computer(board):
    while playerchoice == "o":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "o"
            switchplayer()

while run:
    print()
    printboard(board)
    print()
    playerinput(board)
    switchplayer()
    print()
    checkwin()
    checktie(board)

        
