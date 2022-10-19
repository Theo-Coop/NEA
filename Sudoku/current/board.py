from copy import deepcopy
# have to use deepcopy because using [:] or .copy() still edits the original constant. 
# deepcopy(): a copy of the object is copied into another object. It means that any changes made to a copy of the object do not reflect in the original object. 
# It is needed between classes and in a multi-dimensional list

class Board:
    def __init__(self):
        self.STARTING_BOARD = [
                    [0,7,5,0,0,0,0,1,6],
                    [2,0,0,3,0,0,0,0,0],
                    [0,0,0,0,0,1,7,0,2],
                    [0,2,3,1,0,0,4,0,0],
                    [0,0,0,0,0,7,0,6,0],
                    [7,0,9,4,0,5,0,0,0],
                    [5,3,8,0,1,4,9,0,7],
                    [1,0,7,0,2,8,6,3,4],
                    [0,0,0,0,9,3,0,5,0]
                        ]

        self.board_clear()
        

    def update(self, num, y, x):
        self.editable_board[y-1][x-1] = num

    
    def get_num(self, y, x):
        return self.STARTING_BOARD[y-1][x-1]

    
    def board_clear(self):
        self.editable_board = deepcopy(self.STARTING_BOARD)

    
    def num_valid(self, number, r, c):
        # Check row
        for i in range(len(self.editable_board[0])):
            if self.editable_board[r][i] == number and (r,i) != (r,c):
                return False

        # Check column
        for i in range(len(self.editable_board)):
            if self.editable_board[i][c] == number and (i,c) != (r,c):
                return False

        # Check 3x3 cube
        box_y = r // 3
        box_x = c // 3

        for i in range(box_y * 3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.editable_board[i][j] == number and (i,j) != (r,c):
                    return False

        return True


    def whole_board_valid(self): #Checks if the whole current board is valid
        for r in range(9):
            for c in range(9):
                num = self.editable_board[r][c]
                if num != 0:
                    if self.num_valid(num, r, c) == False:  return False

        return True


    def print_board(self, board):
        print()
        print()
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            
            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")