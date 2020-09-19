
import pygame

pygame.init()

win = pygame.display.set_mode((381,410))

pygame.display.set_caption("TicTacToe")

img_board = pygame.image.load('board.png')
img_cross = pygame.image.load('cross.png')
img_circle = pygame.image.load('circle.png')
img_circle_win = pygame.image.load('circle_win.png')
img_cross_win = pygame.image.load('cross_win.png')
img_draw = pygame.image.load('draw.png')

player = True
run = True

class box():
	def __init__(self,x,y):
		self.x = x + 1
		self.y = y + 2
		self.val = 0
		self.center = [x + 62,y + 62]

	def draw(self,win):
		if self.val == 1:
			win.blit(img_cross,(self.x,self.y))
		if self.val == 2:
			win.blit(img_circle,(self.x,self.y))

	def __str__(self):
		a = "box:("+ str(self.val) + "," + str(self.center)+")"
		return a

l = [[13,27],[135,27],[257,27],[13,149],[135,149],[257,149],[13,271],[135,271],[257,271]]
L = []
for i in l:
    L.append(box(i[0],i[1]))


def redrawGameWindow():
    win.blit(img_board, (0,0))
    for i in L:
        i.draw(win)
    pygame.display.update()

def drawWinner(winner):
    if winner == 0:
        win.blit(img_draw, (0,0))
    if winner == 1:
        win.blit(img_cross_win, (0,0))
    if winner == 2:
        win.blit(img_circle_win, (0,0))
    pygame.display.update()

def FindPossibleMoves():
	possibleMoves = []
	index = 0
	for x in L:
		if x.val == 0:
			possibleMoves.append(index)
		index += 1
	return possibleMoves

def PlayerMove():
	global player
	player = not(player)
	possibleMoves = FindPossibleMoves()

	mpos = pygame.mouse.get_pos()
	D=[]
	for i in possibleMoves:
		distance = ((mpos[0] - L[i].center[0]) ** 2 + (mpos[1] - L[i].center[1]) ** 2) ** 0.5
		D.append(distance)

	possibleMoves[D.index(min(D))]
	return possibleMoves[D.index(min(D))]
	

def AIMove():
	global player
	player = not(player)
	possibleMoves = FindPossibleMoves()

	#can I do a winning move ?
	for index in possibleMoves:
		val = L[index].val
		if val == 0:
			board = L[:]
			board[val] = 2
			a = isWinning(board)
			if a == 2:
				return index

	#can x win next turn ?
	for index in possibleMoves:
		val = L[index].val
		if val == 0:
			board = L[:]
			board[val] = 1
			a = isWinning(board)
			if a == 1:
				return index
	
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
	    if i in [1,3,5,7]:
	        edgesOpen.append(i)
	        
	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
		return move
	

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isWinning(board):
	R1 = [L[0].val,L[1].val,L[2].val]
	R2 = [L[3].val,L[4].val,L[5].val]
	R3 = [L[6].val,L[7].val,L[8].val]
	C1 = [L[0].val,L[3].val,L[6].val]
	C2 = [L[1].val,L[4].val,L[7].val]
	C3 = [L[2].val,L[5].val,L[8].val]
	D1 = [L[0].val,L[4].val,L[8].val]
	D2 = [L[2].val,L[4].val,L[6].val]
	A = [R1,R2,R3,C1,C2,C3,D1,D2]

	for a in A:
		if a[0] == a[1] == a[2] and a[0] != 0:
			if a[0] == 1:
				return 1 # x wins
			else:
				return 2 # o wins
	drawCount = 0
	for a in L:
		if a.val != 0:
			drawCount += 1
	if drawCount == 9:
		return 0 # draw



while run:
	pygame.time.Clock().tick(10)

	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT or keys[pygame.K_t]:
			run = False
		if player:
			if event.type == pygame.MOUSEBUTTONDOWN:
				move = PlayerMove()
				L[move].val = 1
		else:
			pygame.time.delay(500)
			move = AIMove()
			L[move].val = 2

	winner = isWinning(L)
	redrawGameWindow()
	
	if winner == 0 or winner == 1 or winner == 2:
		drawWinner(winner)
		pygame.time.delay(3000)
		run = False


pygame.quit()


