# # import json

# # board = [1,2,3]

# # str_board = json.dumps(board)

# # lst_board = json.loads(str_board)

# # print(type(str_board))

# # print(type(lst_board))

# # lst_board[0] = 4

# # print(lst_board)

# import sqlite3

# con = sqlite3.connect("test.db")

# cur = con.cursor()

# # command1 = ("CREATE TABLE accounts("
# #             "id INTEGER PRIMARY KEY,"
# #             "email TEXT,"
# #             "username TEXT,"
# #             "password TEXT)") 

# # cur.execute(command1)

# username = "Theo234"
# user_id = 4
# # command2 = (f"INSERT INTO accounts VALUES ('{user_id}', 'theo@gmail.com', '{username}', 'Password1!')")


# command3 = ("SELECT password FROM accounts WHERE id = 4")
# cur.execute(command3)

# results = cur.fetchall()
# print(results[0][0])

hashed = b'$2b$12$dgwplqLS1QUYgGKL7Csdd.kJFV8vQhcBQR/uVlc7MCybSEPrpjkve'

str_hashed = hashed.decode()

print(type(hashed))
print(type(str_hashed))
print(str_hashed)