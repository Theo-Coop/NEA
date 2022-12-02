import random

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
    
    print()
    print()


def num_valid(board, num, r, c): # Checks if the current selection is valid
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


def whole_board_valid(board): #Checks if the whole current board is valid
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0:
                if num_valid(board, num, r, c) == False:  return False

    return True









board = [[0 for _ in range(9)] for _ in range(9)]


def shuffle_along():
    # This modifies the board outside the function
    # shuffling_row = [5, 3, 4, 1, 7, 6, 2, 9, 8] # say this is what was shuffled for example
    shuffling_row = [1,2,3,4,5,6,7,8,9]
    random.shuffle(shuffling_row)
    board[0] = shuffling_row.copy()

    # Have to use .copy() so the list doesn't change every time on the board
    
    for i in range(1, 9):
        if i % 3 == 0:
            shuffling_row.insert(0, shuffling_row.pop()) # Shuffle board along 1 place
        else:
            for _ in range(3):
                shuffling_row.insert(0, shuffling_row.pop()) # Shuffle board along 3 places

        board[i] = shuffling_row.copy()


shuffle_along()
print_board(board)


# Switches all the rows
copy_board = board.copy()

for i in range(0, 7, 3): # Goes 0, 3, 6
    # Switch 2 rows
    switch_perms = [0, 1, 2]
    random.shuffle(switch_perms)
    
    for j in range(3):
        board[i+j] = copy_board[switch_perms[j]+i]




# Switch columns
orders = [
    [2,0,1],
    [1,2,0],
    [2,1,0]
]
# These are 3 premade orders for the columns to avoid any repetitions of column swapping

random.shuffle(orders)
print(orders)

for row in board:
    for i in range(0, 7, 3): # 0, 3, 6
        row[0+i], row[1+i], row[2+i] = row[orders[i//3][0]+i], row[orders[i//3][1]+i], row[orders[i//3][2]+i]


print()
print_board(board)
print(whole_board_valid(board))