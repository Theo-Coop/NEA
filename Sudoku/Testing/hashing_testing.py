# import bcrypt


# users = {}

# username = "TheoMC"
# test = "gabecharlie123!easy"

# password = test.encode()
# salt = bcrypt.gensalt()

# hashed = bcrypt.hashpw(password, salt)

# users[username] = hashed




# new_user = "TheoMC"
# new_password_str = "gabecharlie123!easy"
# new_password = new_password_str.encode()


# hash = users[username]

# if bcrypt.checkpw(new_password, hash):
#     print("Yes")
# else:
#     print("No")


# print(users)





import bcrypt

start_text = b"abcde123"

salt = bcrypt.gensalt()
print(salt)

hash = bcrypt.hashpw(start_text, salt)


print(hash)