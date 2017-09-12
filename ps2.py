###### this is the second .py file ###########

####### write your code here ##########


#  board
board= [0,1,2,
        3,4,5,
        6,7,8]

def disp():
	print board[0],'|',board[1],"|",board[2]
	print "----------"
	print board[3],'|',board[4],"|",board[5]
	print "----------"
	print board[6],'|',board[7],"|",board[8]

def isWinner(bo, Player1):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] + bo[8] + bo[9]) >=15) or # across the top
    ((bo[4]+ bo[5] + bo[6]) >=15) or # across the middle
    ((bo[1] + bo[2] + bo[3]) >=15 ) or # across the bottom
    ((bo[7] +bo[4]+bo[1]) =>15) or # down the left side
    ((bo[8] + bo[5] + bo[2] )=>15) or # down the middle
    ((bo[9] + bo[6] + bo[3] )=>15) or # down the right side
    ((bo[7] +  bo[5] + bo[3] )=>15) or # diagonal
    ((bo[9] + bo[5] + bo[1] )=>15)) # diagonal
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
while True:
	print "Welcome to the Game"
	position= 
