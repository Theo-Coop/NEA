import random
from itertools import chain

class generatedBoard:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

        self.shuffle_along()
        self.row_switch()
        self.column_switch()


    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
        
        print()


    def num_valid(self, num, r, c): # Checks if the current selection is valid
        # Check row
        for i in range(len(self.board[0])):
            if self.board[r][i] == num and (r,i) != (r,c):
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][c] == num and (i,c) != (r,c):
                return False

        # Check 3x3 cube
        box_y = r // 3
        box_x = c // 3

        for i in range(box_y * 3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != (r,c):
                    return False
        return True


    def whole_board_valid(self): #Checks if the whole current board is valid
        for r in range(9):
            for c in range(9):
                num = self.board[r][c]
                if num != 0:
                    if self.num_valid(num, r, c) == False:  return False

        return True







    def shuffle_along(self):
        # This modifies the board outside the function
        # shuffling_row = [5, 3, 4, 1, 7, 6, 2, 9, 8] # say this is what was shuffled for example
        shuffling_row = [1,2,3,4,5,6,7,8,9]
        random.shuffle(shuffling_row)
        self.board[0] = shuffling_row.copy()

        # Have to use .copy() so the list doesn't change every time on the board
        
        for i in range(1, 9):
            if i % 3 == 0:
                shuffling_row.insert(0, shuffling_row.pop()) # Shuffle board along 1 place
            else:
                for _ in range(3):
                    shuffling_row.insert(0, shuffling_row.pop()) # Shuffle board along 3 places

            self.board[i] = shuffling_row.copy()



    # Switches all the rows
    def row_switch(self):
        copy_board = self.board.copy()

        for i in range(0, 7, 3): # Goes 0, 3, 6
            # Switch 2 rows
            switch_perms = [0, 1, 2]
            random.shuffle(switch_perms)
            
            for j in range(3):
                self.board[i+j] = copy_board[switch_perms[j]+i]


    # Switch columns
    def column_switch(self):
        orders = [
            [2,0,1],
            [1,2,0],
            [2,1,0]
        ]
        # These are 3 premade orders for the columns to avoid any repetitions of column swapping
        # This switches columns within each 3x3 "box"

        random.shuffle(orders)

        for row in self.board:
            for i in range(0, 7, 3): # 0, 3, 6
                row[0+i], row[1+i], row[2+i] = row[orders[i//3][0]+i], row[orders[i//3][1]+i], row[orders[i//3][2]+i]



        # This switches other columns which contain the same 3 numbers
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
        for row in self.board:
            row[indexes[0][0]], row[indexes[0][1]] = row[indexes[0][1]], row[indexes[0][0]]


    # Run a million times and every board is valid
    # for i in range(1000000):
    #     board = [[0 for _ in range(9)] for _ in range(9)]
    #     shuffle_along()
    #     row_switch()
    #     column_switch()
    #     if whole_board_valid(board) == False:
    #         print("Not valid)

    # print("done")


if __name__ == "__main__":
    board = generatedBoard()
    board.print_board()
    print(board.whole_board_valid())