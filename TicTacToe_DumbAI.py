import time

L = [0,1,2,3,4,5,6,7,8]
board = [" "," "," "," "," "," "," "," "," "]


def FindPossibleMoves():
	possibleMoves = []
	index = 0
	for x in board:
		if x == " ":
			possibleMoves.append(index)
		index += 1
	return possibleMoves
	
def displayBoard(b):
    print('     |     |')
    print('  ' + b[0] + '  |  ' + b[1] + '  |  ' + b[2])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + b[3] + '  |  ' + b[4] + '  |  ' + b[5])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + b[6] + '  |  ' + b[7] + '  |  ' + b[8])
    print('     |     |')
    print("\n")

def AIMove(player):
	opp = notPlayer(player)
	possibleMoves = FindPossibleMoves()
	#can I do a winning move ?
	for i in possibleMoves:
		tempBoard = board[:]
		tempBoard[i] = player
		if isWinning(tempBoard) == player:
			return i
	
	#can x win next turn ?
	for i in possibleMoves:
		tempBoard = board[:]
		tempBoard[i] = opp
		if isWinning(tempBoard) == opp:
			return i
	
	#else
	cornersOpen = []
	for i in possibleMoves:
	    if i in [0,2,6,8]:
	        cornersOpen.append(i)
	        
	if len(cornersOpen) > 0:
		move = selectRandom(cornersOpen)
		return move
	
	if 4 in possibleMoves:
	    move = 4
	    return move
	
	edgesOpen = []
	for i in possibleMoves:
	    if x in [1,3,5,7]:
	        edgesOpen.append(i)
	        
	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
		return move
	pass

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def notPlayer(player):
	if player == "x":
		return "o"
	else:
		return "x"

def isWinning(board):
	R1 = [board[0],board[1],board[2]]
	R2 = [board[3],board[4],board[5]]
	R3 = [board[6],board[7],board[8]]
	C1 = [board[0],board[3],board[6]]
	C2 = [board[1],board[4],board[7]]
	C3 = [board[2],board[5],board[8]]
	D1 = [board[0],board[4],board[8]]
	D2 = [board[2],board[4],board[6]]
	A = [R1,R2,R3,C1,C2,C3,D1,D2]

	for line in A:
		if line[0] == line[1] == line[2] and line[0] != " ":
			if line[0] == "x":
				return "x" # x wins
			else:
				return "o" # o wins
	if not(" " in board):
		return " " # draw
	pass

player = "x"
run = True

while run:

	#time.sleep(3)

	if player == "x":
		move = AIMove(player)
		board[move] = "x"
	else:
		move = AIMove(player)
		board[move] = "o"

	player = notPlayer(player)

	#displayBoard(board)
	winner = isWinning(board)
	
	if winner == "x" or winner == "o" or winner == " ":
		print("winner="+winner)
		run = False

