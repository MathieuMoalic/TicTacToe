import random

class Random_AI:
    def __init__(self, game):
        self.game = game
        self.board = game.board
        self.tile = "o"
        
    def turn(self):
        # a = input("move: ")
        i,j = self.random_move()
        self.board[i][j] = self.tile
        print("AI played")
        self.game.print_board()
        
    def prossible_moves(self):
        list_moves = []
        for i,row in enumerate(self.board):
            for j,tile in enumerate(row):
                if tile is '':
                    list_moves.append((i,j))
        return list_moves
    
    def random_move(self):
        m = random.choice(self.prossible_moves())
        return m                