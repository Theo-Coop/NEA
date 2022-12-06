import random
import board_generation_testing

def print_board():
    for i in range(len(full_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        
        for j in range(len(full_board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(full_board[i][j])
            else:
                print(str(full_board[i][j]) + " ", end="")

def find_empty(): # find empty space on board
    for i in range(len(full_board)):
        for j in range(len(full_board[0])):
            if full_board[i][j] == 0:
                return (i, j) # row, column

    return False # There are no empty squares


def solve():
    find = find_empty()
    if find == False:
        return True
    else:
        row, col = find[0], find[1]

    for i in range(1, 10):
        if full_board.num_valid(i, row, col):
            full_board[row][col] = i

            if solve(full_board):
                return True
            else:
                full_board[row][col] = 0

    return False

full_board = board_generation_testing.generatedBoard()

full_board.print_board()
print(full_board.whole_board_valid())


dict_nums_to_be_removed = {
    "easy": (36, 46),
    "medium": (32, 35),
    "hard": (28, 31)
}

difficulty = "easy"
nums_to_be_removed = random.randint(dict_nums_to_be_removed[difficulty])

print(nums_to_be_removed)