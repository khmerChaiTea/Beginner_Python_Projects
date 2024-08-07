# 12 Beginner Python Projects with https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org

import math
import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Initialize an empty 3x3 board
        self.current_winner = None # Tracks the current winner ('X', 'O', or None)
        
    def print_board(self):
        # Prints the current board state
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |') # separators
            
    @staticmethod #do not need a self
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        # Prints the board with numbers indicating each position
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |') # separators
            
    def available_moves(self):
        # Returns a list of available moves (indices where the board is empty)
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
        
    def empty_squares(self):
        # Checks if there are empty squares left on the board
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
        # return len(self.available_moves())
        
    def make_move(self, square, letter):
        # Attempts to place the letter on the board at the specified square
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all these!
        # first let's check the rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check columns
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals
        # only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal (by order of numbers)
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal (by order of numbers)
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all of these fail
        return False
        
def play(game, x_player, o_player, print_game=True):
    # return the winner of the game(the letter)! or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because
    # we'll just return that which breaks the loop)
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just an empty line
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
            
        # a tiny pause
        if print_game:
            time.sleep(.8)
            
    if print_game:
        print('It\'s a tie!')
            
if __name__ == '__main__':

    x_player = HumanPlayer('X') # Example: HumanPlayer or any other player class
    o_player = GeniusComputerPlayer('O')    # Example: RandomComputerPlayer or any other player class
    t = TicTacToe() # t is an instance of TicTacToe
    play(t, x_player, o_player, print_game= True)   # Start the game
