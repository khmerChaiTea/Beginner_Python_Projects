# 12 Beginner Python Projects with https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org

import math
import random

# set up Player and Game to two separate classes
# base Player object, super class call this object
class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
    
    # we want all player to get their next move
    def get_move(self, game):
        pass

# using inheritance to create a random computer player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # we're going to check that this is a correct value  by trying to cast
            # it to an integer, and if it's not , then we say it's invalid
            # if that spot is not available on the board, we say it's invalid
            try:
                val = int(square)
                if  val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print ('Invalid square. Try again.')
                
        return val