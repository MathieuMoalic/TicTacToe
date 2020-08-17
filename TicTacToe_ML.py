import time
import numpy as np
import os

nodes = 16
#input of NN = number of columns in data
#
#output of NN = chosen move
class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],nodes) 
        self.weights2 = np.random.rand(nodes,1)                 
        self.y = y
        self.output = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function
        # with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) * sigmoid(self.output,deriv=True)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2 * (self.y - self.output) * sigmoid(self.output,deriv=True), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, y):
        self.output = self.feedforward()
        self.backprop()


def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

#game functions
def FindPossibleMoves(board):
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

def AIMove(board,player):
	opp = notPlayer(player)
	possibleMoves = FindPossibleMoves(board)
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

def AIrandomMove(board):
	possibleMoves = FindPossibleMoves(board)
	np.random.shuffle(possibleMoves)
	move = possibleMoves[0]
	return move

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

def game(train=False):
	player = "x"
	board = [" "," "," "," "," "," "," "," "," "]
	train_data = []
	run = True
	while run:

		#time.sleep(3)

		if player == "x":
			move = AIrandomMove(board)
			board[move] = "x"
			data = board + [move]
			train_data.append(data)
		else:
			move = AIrandomMove(board)
			board[move] = "o"

		player = notPlayer(player)

		#displayBoard(board)
		winner = isWinning(board)
	
		if winner == "x":
			if train:
				np.save("train_data/{}.npy".format(str(int(time.time_ns()))), np.array(train_data))
			run = False
		if winner == "o" or winner == " ":
			run = False
	pass

def createData():
	for i in range(30000):
		game(train=True)

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


#file = np.load("train_data/"+ str(files[3449]))
#displayBoard(file[-1])

def training():
	files = [f for f in os.listdir('train_data')]
	board = [" "," "," "," "," "," "," "," "," ",5]
	NN = NeuralNetwork(board,y)
	for i in range(1500): # trains the NN 1,500 times
		if i % 100 ==0: 
			print ("for iteration # " + str(i) + "\n")
			print ("Input : \n" + str(X))
			print ("Actual Output: \n" + str(y))
			print ("Predicted Output: \n" + str(NN.feedforward()))
			print ("Loss: \n" + str(np.mean(np.square(y - NN.feedforward())))) # mean sum squared loss
			print ("\n")
		file=files[i]
		for j in file:
			X=file[j]
			y=files[0][4]
			NN.train(X, y)

training()