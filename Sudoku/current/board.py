class FreePlayBoard:
    def __init__(self):
        self.new_board()

    
    def new_board(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)] # Create empty 9x9 2D list full of zeroes


    def update(self, num, r, c):
        self.board[r][c] = num

    
    def reset_value(self, r, c):
        self.board[r][c] = 0 


    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r, c)

        return False # There are no empty cells

    
    def num_valid(self, number, r, c):
        # Check row
        for i in range(len(self.board[0])):
            if self.board[r][i] == number and (r,i) != (r,c):
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][c] == number and (i,c) != (r,c):
                return False

        # Check 3x3 cube
        box_y = r // 3
        box_x = c // 3

        for i in range(box_y * 3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == number and (i,j) != (r,c):
                    return False

        return True


    def whole_board_valid(self): #Checks if the whole current board is valid
            for r in range(9):
                for c in range(9):
                    num = self.board[r][c]
                    if num != 0:
                        if self.num_valid(num, r, c) == False:  return False

            return True

    # def print_board(self, board):
    #         print()
    #         print()
    #         for i in range(len(board)):
    #             if i % 3 == 0 and i != 0:
    #                 print("- - - - - - - - - - - - ")
                
    #             for j in range(len(board[0])):
    #                 if j % 3 == 0 and j != 0:
    #                     print(" | ", end="")

    #                 if j == 8:
    #                     print(board[i][j])
    #                 else:
    #                     print(str(board[i][j]) + " ", end="")