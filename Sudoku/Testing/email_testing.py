import re

def validate_email(email):
    regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$')
    return regex.fullmatch(email)


while True:
    email = input("Enter email address: ")

    if validate_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")
