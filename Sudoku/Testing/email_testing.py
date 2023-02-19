import re

# def validate_email(email):
#     regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$')
#     return regex.fullmatch(email)


# while True:
#     email = input("Enter email address: ")

#     if validate_email(email):
#         print("Valid email address")
#     else:
#         print("Invalid email address")




# Password regex testing

def validate_password(password):
    regex = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
    return regex.fullmatch(password)


while True:
    pw = input("Enter password: ")

    if validate_password(pw):
        print("Valid pw")
    else:
        print("Not valid")