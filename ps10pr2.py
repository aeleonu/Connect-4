#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#

from ps10pr1 import Board

# Write your class below.

class Player:
    """ Represent a player of the Connect Four game. """
    
    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object. """
        a = 'Player ' + str(self.checker)
        return a

    def opponent_checker(self):
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """  accepts a Board object as a parameter and returns the
             column where the player wants to make the next move. """
        col = int(input(""" enter a column: """))
        while col < 0 or col >= board.width:
            print('Try Again!')
            col = int(input(""" enter a column: """))

        self.num_moves += 1
        return col
                      
        
        
        
        
    
