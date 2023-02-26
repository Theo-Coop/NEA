import json

board = [1,2,3]

str_board = json.dumps(board)

lst_board = json.loads(str_board)

print(type(str_board))

print(type(lst_board))

lst_board[0] = 4

print(lst_board)