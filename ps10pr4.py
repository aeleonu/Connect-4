#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# An AI Player for use in Connect Four
#

import random
from ps10pr3 import *

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object. """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object. """
        s = 'Player' + self.checker + ' (' + self.tiebreak + ' , ' + str(self.lookahead) + ')'
        return s
        
    def max_score_column(self, scores):
         """ Takes a list scores containing a score for each column of the board,
         and that returns the index of the column with the maximum score. """
         max_scores = max(scores)
         index_list = []
         for i in range(len(scores)):
             if scores[i] == max_scores:
                 index_list += [i]
         if len(index_list) == 1:
                 return index_list[0]
         if len(index_list) > 1:
             if self.tiebreak == "LEFT":
                 i = index_list[0]
             elif self.tiebreak == "RIGHT":
                 i = index_list[-1]
             elif self.tiebreak == "Random":
                 i = random.choice(index_list)
         return i

    def scores_for(self, board):
        """ Takes a Board object board and determines the called AIPlayer‘s scores for the columns in board. """
        scores = list([0] * board.width)
        for c in range(len(scores)):
            if board.is_full() == True:
                scores[c] = 50
            elif board.can_add_to(c) == False:
                scores[c] = -1
            elif board.is_win_for(self.checker) == True:
                scores[c] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[c] = 0
            elif self.lookahead == 0:
                scores[c] = 50
            else:
                board.add_checker(self.checker, c)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                print(opp_scores)
                if max(opp_scores) == 100:
                    scores[c] = 0
                elif max(opp_scores) == 0:
                    scores[c] = 100
                else:
                    scores[c] = 50
                board.remove_checker(c)
        return scores
        
        
    def next_move(self, board):
        """ overrides next_move method inherited from player. """
        board = Board(board.height, board.width)
        col = self.scores_for(board)
        self.num_moves += 1
        return self.max_score_column(self.scores_for(board))
        
        
    
