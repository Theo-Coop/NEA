import random
import board_generation_testing


def find_empty(): # find empty space on board
    for i in range(len(full_board.board)):
        for j in range(len(full_board.board[0])):
            if full_board.board[i][j] == 0:
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
            full_board.board[row][col] = i

            if solve():
                return True
            else:
                full_board.board[row][col] = 0

    return False


def remove_square(tuple):
    r, c = tuple[0], tuple[1]
    full_board.board[r][c] = 0


full_board = board_generation_testing.generatedBoard()

full_board.print_board()



dict_nums_to_be_removed = {
    "easy": (35, 45), # Keep: (36, 46)
    "medium": (46, 49), # Keep: (32, 35)
    "hard": (50, 53) # Keep: (28, 31)
}


difficulty = "easy"
a, b = dict_nums_to_be_removed[difficulty][0], dict_nums_to_be_removed[difficulty][1]
nums_to_be_removed = random.randint(a,b)


cells = [(r, c) for r in range(9) for c in range(9)]

random.shuffle(cells)


for i in range(nums_to_be_removed):
    remove_square(cells[i])

print()
full_board.print_board()
