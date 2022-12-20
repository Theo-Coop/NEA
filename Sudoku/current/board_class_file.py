class GameBoard:
    def __init__(self):
        self.new_board()

    
    def new_board(self):
        self.game_board = [[0 for _ in range(9)] for _ in range(9)] # Create empty 9x9 2D list full of zeroes


    def update(self, num, r, c):
        self.game_board[r][c] = num

    
    def reset_value(self, r, c):
        self.game_board[r][c] = 0 


    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.game_board[r][c] == 0:
                    return (r, c)

        return False # There are no empty cells

    
    def num_valid(self, number, r, c):
        # Check row
        for i in range(len(self.game_board[0])):
            if self.game_board[r][i] == number and (r,i) != (r,c):
                return False

        # Check column
        for i in range(len(self.game_board)):
            if self.game_board[i][c] == number and (i,c) != (r,c):
                return False

        # Check 3x3 cube
        box_y = r // 3
        box_x = c // 3

        for i in range(box_y * 3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.game_board[i][j] == number and (i,j) != (r,c):
                    return False

        return True


    def whole_board_valid(self): #Checks if the whole current board is valid
            for r in range(9):
                for c in range(9):
                    num = self.game_board[r][c]
                    if num != 0:
                        if self.num_valid(num, r, c) == False:  return False

            return True

    
    def instant_solve(self):
        find = self.find_empty()
        if find == False:
            return True
        else:
            row, col = find[0], find[1]

        for i in range(1, 10):
            if self.num_valid(i, row, col):
                self.game_board[row][col] = i

                if self.instant_solve():
                    return True
                else:
                    self.game_board[row][col] = 0

        return False


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