# Board class used in the Free Play and New Game moddes
class GameBoard:
    def __init__(self):
        self.new_board() # Call the new_board function when starting this class

    
    def new_board(self):
        self.game_board = [[0 for _ in range(9)] for _ in range(9)] # Create empty 9x9 2D list full of zeroes


    def update(self, num, r, c): # Update the board with the number supplied
        self.game_board[r][c] = num

    
    def reset_value(self, r, c): # Reset the number at the co-ordinates supplied
        self.game_board[r][c] = 0 


    def is_board_full(self): # Used in the New Game mode to congratulate the user upon completion of the puzzle
        for r in range(9):
            for c in range(9):
                if self.game_board[r][c] == 0:
                    return False      # The board still has empty numbers on it

        return True   # The board is full


    def clear_user_inputs(self, start_board): # Used inn the New Game mode, where the numbers the user inputted
        # should be cleared, but the starting board numbers should remain
        for r in range(9):
            for c in range(9):
                if self.game_board[r][c] != 0 and start_board[r][c] == 0: # If there is a number the user entered
                    # and there is no number that is on the starting board, clear the number
                    self.game_board[r][c] = 0


    def find_empty(self): # Find an empty cell and return the row and column of it
        for r in range(9):
            for c in range(9):
                if self.game_board[r][c] == 0:
                    return (r, c)

        return False # There are no empty cells

    
    # Check if a given number is valid in the given cell
    def num_valid(self, number, r, c):
        # Check row
        for i in range(len(self.game_board[0])):
            if self.game_board[r][i] == number and (r,i) != (r,c): # check if there are duplicate nums in the row and "i" is not the same as the column
                return False

        # Check column
        for i in range(len(self.game_board)):
            if self.game_board[i][c] == number and (i,c) != (r,c): # check if there are duplicate nums in the column and "i" is not the same as the row
                return False

        # Check 3x3 cube for duplicate number
        box_y = r // 3
        box_x = c // 3

        for i in range(box_y * 3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.game_board[i][j] == number and (i,j) != (r,c):
                    return False

        return True


    def whole_board_valid(self): # Checks if the whole current board is valid
            for r in range(9):
                for c in range(9):
                    num = self.game_board[r][c]
                    if num != 0:
                        if self.num_valid(num, r, c) == False:  return False

            return True

    # Instant solve function
    def instant_solve(self):
        find = self.find_empty() # Find empty slot
        if find == False:
            # Board is solved
            return True
        else:
            row, col = find[0], find[1]

        for i in range(1, 10): # Checks each number
            if self.num_valid(i, row, col):
                self.game_board[row][col] = i # Set the number on the board if that number is valid

                if self.instant_solve(): # Recursive call of this function
                    return True
                else:
                    self.game_board[row][col] = 0 # Backtrack by setting the number on the board to 0

        return False


    # A function used to print the board, *only used for testing* as it prints out in the terminal
    def print_board(self):
            print()
            print()
            for i in range(len(self.game_board)):
                if i % 3 == 0 and i != 0:
                    print("- - - - - - - - - - - - ")
                
                for j in range(len(self.game_board[0])):
                    if j % 3 == 0 and j != 0:
                        print(" | ", end="")

                    if j == 8:
                        print(self.game_board[i][j])
                    else:
                        print(str(self.game_board[i][j]) + " ", end="")