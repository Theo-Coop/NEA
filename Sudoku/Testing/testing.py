import re

user_password = "Password1"


regex = re.compile(r'^(?=.*?[0-9])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[#?!@$%^&*_-]).{8,}$')
if regex.fullmatch(user_password):
    print("Hooray!")
else:
    print("no")
