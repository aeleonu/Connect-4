class Board:
    # Function 1
    def __init__(self, height, width):
        """ constructs a new Board object by initializing three atributes height, width, and slots. """
        self.width = width
        self.height = height
        self.slots = [[' '] * self.width for row in range(self.height)]

    # Function 2
    def  __repr__(self):
        """  returns a string representing a Board object. """
        s = ''
        for row in range(self.height):
            s += '|'

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'

        for col in range(self.width):
            s += '--'
        s += '\n' + ' '
        for col in range(self.width):
            s += str(col % 10)+ ' '
        return s
    
    # Function 3
    def add_checker(self, checker, col):
        """ that accepts two inputs checker and col to add checker to the appropriate row and column in the board. """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1

        self.slots[row - 1][col] = checker
        
    # Function 4
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player object’s opponent. """
        assert(checker == 'X' or checker == 'O')
        if checker == 'X':
            return 'O'
        elif checker == 'O':
            return 'X'
        
    # Function 5
    def reset(self):
        """  reset the Board object on which it is called by setting all slots to contain a space character. """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                    self.slots[row][col] = ' '


    # Function 6                
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    # Function 7
    def can_add_to(self, col):
        """  returns True if it is valid to place a checker in the column col on the calling Board object.
             otherwise returns False. """
        if col < 0 or col > self.width - 1:
            return False
        if self.slots[0][col] == ' ':
            return True
        else:
            return False
    
    # Function 8
    def is_full(self):
        """  returns True if the called Board object is completely full of checkers, and returns False otherwise. """

        for col in range(self.width):
            if self.can_add_to(col) == False:
                return True
            else:
                return False

    # Function 9
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing. """
        row = 0
        while row < self.height-1 and self.slots[row][col] == ' ':
            row += 1
        if row == 0:
            self.slots[row][col] = ' '
        else:
            self.slots[row][col] = ' '

    # Helper Functions                          
    def is_horizontal_win(self, checker):
        """ Determines if there is a horizontal win. """
        assert(checker == 'X' or checker == 'O')
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
    def is_vertical_win(self, checker):
        """ Determines if there is a vertical win. """
        assert(checker == 'X' or checker == 'O')
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
                
    def is_up_diagonal_win(self, checker):
        """ determines if there is an upward diagonal win. """
        assert(checker == 'X' or checker == 'O')
        for row in range(self.height - 3):
            for col in range(3, self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col - 1] == checker and \
                   self.slots[row + 2][col - 2] == checker and \
                   self.slots[row + 3][col - 3] == checker:
                    return True
                
    def is_down_diagonal_win(self, checker):
        """ Determines if there is a win diagonally. """
        assert(checker == 'X' or checker == 'O')
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
                
    def is_win_for(self, checker):
        """  accepts a parameter checker that is either 'X' or 'O', and
             returns True if there are four consecutive slots containing checker on the board.
             Otherwise, it should return False. """

        assert(checker == 'X' or checker == 'O')
        

        if self.is_horizontal_win(checker) == True:
            return True
        if self.is_vertical_win(checker) == True:
            return True
        if self.is_up_diagonal_win(checker) == True:
            return True
        if self.is_down_diagonal_win(checker) == True:
            return True
        else:
            return False
        
