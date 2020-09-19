class Human:
    def __init__(self, game):
        self.game = game
        self.board = game.board
        self.tile = "x"
        
    def turn(self):
        a = input("move: ")
        i,j = int(a[0]),int(a[1])
        self.board[i][j] = self.tile
        self.game.print_board()