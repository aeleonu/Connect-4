#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the game
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
def process_move(player, board):
    ''' takes two parameters: a Player object for the player
        whose move is being processed, and a Board object for
        the game that is being played. '''
    print("Player X's Turn" or "Player O's Turn.")
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    b = player.num_moves
    print(board)
    if board.is_win_for(player.checker) == True:
        print(" Player X wins in ", b, "moves.")
        print(" Congragulations!" )
        return True
    elif board.is_full() == True:
        print(" It's a tie! ")
        return True
    else:
        return False
                
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)

    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board


class RandomPlayer(Player):
        
    def next_move(self, board):
        new_list = [col for col in range(0, board.width) if board.can_add_to(col) == True ]
        col = random.choice(new_list)
        while col < 0 or col >= board.width:
            print('Try Again!')
            col = int(input(""" enter a column: """))

        self.num_moves += 1
        return col
        
    
