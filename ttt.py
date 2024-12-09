import random

board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
currentPlayer = "X"
winner = None
gamestart = True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])



def playerinput(board):
    inp = int(input("enter a number from 1-9 : "))
    if inp >= 1 and inp <= 9 and board[inp-1] == str(inp):
        board[inp-1] = currentPlayer
    else:
        print("oops error")

def check1(board):
    global winner
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        return True
    
def check2(board):
    global winner
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]:
        winner = board[2]
        return True
    
def check3(board):
    global winner
    if board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        return True
    

def Turnchange():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def compmove(board):
    while currentPlayer == "O":
        position = random.randint(1, 9)
        if board[position - 1] == str(position):
            board[position - 1] = "O"
            Turnchange()
            




def wincheck(board):
    global gamestart
    if check1(board) or check2(board) or check3(board):
        print(f"Th winner is {winner}")
        gamestart = False
        printBoard(board)
    elif board[0] != "1" and board[1] != "2" and board[2] != "3" and board[3] != "4" and board[4] != "5" and board[5] != "6" and board[6] != "7" and board[7] != "8" and board[8] != "9":
        print("tie")
        gamestart = False
        printBoard(board)
    
    


    

while gamestart:
    printBoard(board)
    playerinput(board)
    wincheck(board)
    Turnchange()
    compmove(board)
    wincheck(board)

