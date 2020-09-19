from human import Human 
from random_AI import Random_AI 

class TicTacToe:
    def __init__(self):
        self.board = [['','',''],['','',''],['','','']]
        self.lines = [
            self.board[0],
            self.board[1],
            self.board[2],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]
        self.p1 = Human(self)
        self.p2 = Random_AI(self)
        self.print_board()
        self.game_loop()
        
    def game_loop(self):
        while True:
            self.p1.turn()
            if self.game_ended("x"):
                break
            self.p2.turn()
            if self.game_ended("o"):
                break
        
    def game_ended(self, s):
        for line in self.lines:
            if all( tile is s for tile in line ):
                print(f"{s} won")
                return True
        return False
        
    def print_board(self):
        for row in self.board:
            print(row)
        print("\n")
    
if __name__ == "__main__":
    board = TicTacToe()