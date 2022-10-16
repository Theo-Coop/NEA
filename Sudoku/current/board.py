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
        self.print_board(self.editable_board)

    
    def get_num(self, y, x):
        return self.STARTING_BOARD[y-1][x-1]

    
    def board_clear(self):
        self.editable_board = deepcopy(self.STARTING_BOARD)
        self.print_board(self.editable_board)
        self.print_board(self.STARTING_BOARD)



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