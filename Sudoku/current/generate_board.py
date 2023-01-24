import random

# This is a constant, and a dictionary which stores the range of numbers that correlates to difficulty
# The "keep" comments shows the range of values that will be kept on the board
DICT_NUMS_TO_BE_REMOVED = {
    "easy": (35, 45), # Keep: (36, 46)
    "medium": (46, 49), # Keep: (32, 35)
    "hard": (50, 53) # Keep: (28, 31)
}


# A class to generate a random board that takes a "difficulty" input as a parameter
class GenerateBoard:
    def __init__(self):
        pass

    
    def create_board(self, difficulty):
        # create an empty starting board
        self.starting_board = [[0 for _ in range(9)] for _ in range(9)]

        # Fill in 15 random squares with a random number according to the rules of Sudoku
        for num in range(13):
            num = random.randint(1,9)
            r = random.randint(0,8)
            c = random.randint(0,8)

            while not self.valid(num, r, c): # If the current selection isn't random, choose a new random square and number
                num = random.randint(1,9)
                r = random.randint(0,8)
                c = random.randint(0,8)



            self.starting_board[r][c] = num

        self.solve()


        # The two numbers of the difficulty range
        a, b = DICT_NUMS_TO_BE_REMOVED[difficulty][0], DICT_NUMS_TO_BE_REMOVED[difficulty][1]
        nums_to_be_removed = random.randint(a,b) # Generate a random number of squares to be removed based on the difficulty


        # Generate a random list of cells
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)   


        # Clear the cell
        for i in range(nums_to_be_removed):
            self.remove_square(cells[i])

        
        return self.starting_board # Return the board


    # Function for printing the board for debugging purposes
    def print_board(self):
        for i in range(len(self.starting_board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            
            for j in range(len(self.starting_board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.starting_board[i][j])
                else:
                    print(str(self.starting_board[i][j]) + " ", end="")


    def find_empty(self): # find empty space on board
        for i in range(len(self.starting_board)):
            for j in range(len(self.starting_board[0])):
                if self.starting_board[i][j] == 0:
                    return (i, j) # row, column

        return False # There are no empty squares


    def valid(self, num, r, c): # Checks if the current selection is valid
        # Check row
        for i in range(len(self.starting_board[0])):
            if self.starting_board[r][i] == num:
                return False

        # Check column
        for i in range(len(self.starting_board)):
            if self.starting_board[i][c] == num:
                return False

        # Check 3x3 cube
        box_y = r // 3
        box_x = c // 3

        for i in range(box_y * 3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.starting_board[i][j] == num:
                    return False

        return True


    # Solve function
    def solve(self):
        find = self.find_empty()
        if find == False:
            return True
        else:
            row, col = find[0], find[1]

        for i in range(1, 10):
            if self.valid(i, row, col):
                self.starting_board[row][col] = i

                if self.solve():
                    return True
                else:
                    self.starting_board[row][col] = 0

        return False


    # Clear the cell specified
    def remove_square(self, tuple):
        r, c = tuple[0], tuple[1]
        self.starting_board[r][c] = 0


if __name__ == "__main__":
    GenerateBoard("easy")