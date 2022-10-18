def print_board(board):
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

def find_empty(board): # find empty space on board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column

    return False # There are no empty squares

def valid(board, num, r, c): # Checks if the current selection is valid
    # Check row
    for i in range(len(board[0])):
        if board[r][i] == num and (r,i) != (r,c):
            return False

    # Check column
    for i in range(len(board)):
        if board[i][c] == num and (i,c) != (r,c):
            return False

    # Check 3x3 cube
    box_y = r // 3
    box_x = c // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != (r,c):
                return False
    return True

def solve(board):
    # print_board(board)
    # print("                 ")
    # print("                 ")
    find = find_empty(board)
    if find == False:
        return True
    else:
        row, col = find[0], find[1]

    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True
            else:
                board[row][col] = 0

    return False
 

bo = [
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


print("                            ")
print("Original board:")
print("                            ")
print_board(bo)
solve(bo)
print("____________________________")
print("                            ")
print("Solved board:")
print("                            ")
print_board(bo)
print("                            ")
print("                            ")