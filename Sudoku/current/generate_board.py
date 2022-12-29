import random
from itertools import chain


# This is a constant, and a dictionary which stores the range of numbers that correlates to difficulty
# The "keep" comments shows the range of values that will be kept on the board
DICT_NUMS_TO_BE_REMOVED = {
    "easy": (35, 45), # Keep: (36, 46)
    "medium": (46, 49), # Keep: (32, 35)
    "hard": (50, 53) # Keep: (28, 31)
}


# A class to generate a random board that takes a "difficulty" input as a parameter
class GenerateBoard:
    def __init__(self, difficulty):

        # Sets the difficulty as the input
        self.difficulty = difficulty


        # create an empty starting board
        self.starting_board = [[0 for _ in range(9)] for _ in range(9)]

        # Calls the functions to modify the board
        self.shuffle_along()
        self.row_switch()
        self.column_switch()


        # The two numbers of the difficulty range
        a, b = DICT_NUMS_TO_BE_REMOVED[difficulty][0], DICT_NUMS_TO_BE_REMOVED[difficulty][1]
        nums_to_be_removed = random.randint(a,b) # Generate a random number of squares to be removed based on the difficulty


        # Generate a random list of cells
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)   


        # Clear the cell
        for i in range(nums_to_be_removed):
            self.remove_square(cells[i])




    def shuffle_along(self):
        # This modifies the board outside the function

        shuffling_row = [1,2,3,4,5,6,7,8,9]
        random.shuffle(shuffling_row)
        self.starting_board[0] = shuffling_row.copy()
        # Have to use .copy() so the list doesn't change every time on the board
        

        # Only "shuffle" the shuffling row and then copy that into the actual "starting_board" variable
        for i in range(1, 9):
            if i % 3 == 0:
                # This takes the last item, pops it and inserts it at the front, essentially "shuffling" everything one place to the righ
                shuffling_row.insert(0, shuffling_row.pop()) # Shuffle board along 1 place
            else:
                for _ in range(3):
                    shuffling_row.insert(0, shuffling_row.pop()) # Shuffle board along 3 places

            self.starting_board[i] = shuffling_row.copy()



    # Clear the cell specified
    def remove_square(self, tuple):
        r, c = tuple[0], tuple[1]
        self.starting_board[r][c] = 0


    # Switches rows inside each 3x3 "box"
    def row_switch(self):
        # A temp copy of the original board to hold the rows permutations
        copy_board = self.starting_board.copy()


        for i in range(0, 7, 3): # Goes 0, 3, 6
            # Switch 2 rows
            switch_perms = [0, 1, 2]
            random.shuffle(switch_perms)
            
            for j in range(3):
                self.starting_board[i+j] = copy_board[switch_perms[j]+i]


    # Switch columns inside each 3x3 "box"
    def column_switch(self):
        # These are 3 premade orders for the columns to avoid any repetitions of column swapping
        orders = [
            [2,0,1],
            [1,2,0],
            [2,1,0]
        ]


        random.shuffle(orders)

        for row in self.starting_board:
            for i in range(0, 7, 3): # 0, 3, 6
                
                # Switch the columns around
                row[0+i], row[1+i], row[2+i] = row[orders[i//3][0]+i], row[orders[i//3][1]+i], row[orders[i//3][2]+i]



        # This switches other columns which contain the same 3 numbers
        # Creates a single list of the orders
        flatten_list = list(chain.from_iterable(orders))

        indexes = {
            0: [],
            1: [],
            2: []
        }

        # Gets the indexes for each of the same "columns" and stores them in a dictionary
        for i in range(len(flatten_list)):
            indexes[flatten_list[i]].append(i)


        # Switch two columns across the board (only 2 because if you switch all 3 it does not make it any more random
        # It only "moves" around columns but if you switch 2, each row doesn't just repeat 3 numbers 3 times)
        for row in self.starting_board:
            row[indexes[0][0]], row[indexes[0][1]] = row[indexes[0][1]], row[indexes[0][0]]





    # This creates a shuffled board with no numbers removed

    # I ran this a million times and every board was valid using the rules of Sudoku
    
    # for i in range(1000000):
    #     board = [[0 for _ in range(9)] for _ in range(9)]
    #     shuffle_along()
    #     row_switch()
    #     column_switch()
    #     if whole_board_valid(board) == False:     # Used my valid functions used in the actual solver
    #         print("Not valid)

    # print("done")

    # It printed "done" with 0 "Not valid" statements printed