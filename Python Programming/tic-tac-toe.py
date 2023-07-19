import random
import time

# print the current round
def printRound(round):
    print("\n####################################\n")
    print(f"\n############# Round #{round} #############\n")
    print("\n####################################\n")


# print the updated board
def printBoard(board):
    print("Current board: ")
    print("\n------------------------------------\n")
    print("    0   1   2")
    for i in range(3):
        print(f"{i}   {board[i][0]}   {board[i][1]}   {board[i][2]}")
    print("\n------------------------------------\n")
    time.sleep(1)

# randomly generate a computer move
def computerMove(computer, board):
    print("Player '" + computer + "' turn \n")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if(board[row][col] == "."):
            board[row][col] = computer
            print(" Computer move Registered. \n")
            break
    time.sleep(0.5)

# use user input to generate player move      
def playerMove(player, board):
    print("Player '" + player + "' turn \n")
    while True:
        row = input("What row? ")
        col = input("What column? ")
        if row.isdigit() and col.isdigit() and (int(row) in range(0,3)) and (int(col) in range(0,3)) and board[int(row)][int(col)] == ".":
            # convert string to int
            row = int(row)
            col = int(col)
            
            # collect response it's valid
            response = input(f"Place {player} at row {row}, column {col}? [y/n] ").lower()
            while(response != "x" and response != "y"):
                response = input("Not a valid option. Choose x or y: ")

            # if response is y, place move
            if response.lower() == "y":
                board[row][col] = player
                print(" Move placed! \n")
                break
            
            else:
                print(" Move canceled. Try again.\n")
        else:
            print("Invalid selection. Choose 0, 1 or 2 for row and column")
       
    time.sleep(0.5)

# checks whether the player or computer wins
def checkForWin(player, board):
    for i in range(3):
        # check each row
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # check each col
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # check diagonal from top-left to bottom-right
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True    
    # check diagonal from top-right to bottom-left
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# checks for stalemate
def checkForTie(board):
    # check if all cells in board are occupied
    if all(cell != "." for row in board for cell in row):
        return True
    return False

# creates a game
def playGame():
    # initialize board, player and computer
    board = [["." for _ in range(3)] for _ in range(3)]
    player = input("X or O? ").upper()
    while(player != "X" and player != "O"):
        print("Invalid Response. Choose X or O.")
        player = input("X or O? ").upper()
    computer = "O" if player == "X" else "X"

    # initialize round and update after player and computer have moved 
    round = 1
    while True:
        # if player chose X they go first
        if player == "X":
            printRound(round)
            printBoard(board)

            playerMove(player, board)
            printBoard(board)
        
            # check if the player won
            if(checkForWin(player, board)):
                print(f"Congratulations! {player} Wins!")
                break

            # check if there is a tie
            if(checkForTie(board)):
                print("It's a tie!")
                break

            computerMove(computer, board)
            printBoard(board)

            # check if the computer won
            if(checkForWin(computer, board)):
                print(f"You lose! {computer} Wins!")
                break
            
            # check if there is a tie
            if(checkForTie(board)):
                print("It's a tie!")
                break
            
            round += 1
            
        # if computer is X, they go first
        else:
            printRound(round)
            printBoard(board)

            computerMove(computer, board)
            printBoard(board)
            if(checkForWin(computer, board)):
                print(f"You lose! {computer} Wins!")
                break
            
            if(checkForTie(board)):
                print("It's a tie!")
                break
                
            playerMove(player, board)
            printBoard(board)
            if(checkForWin(player, board)):
                print(f"Congratulations! {player} Wins!")
                break
            
            if(checkForTie(board)):
                print("It's a tie!")
                break

            round += 1
                
# create a game
playGame()