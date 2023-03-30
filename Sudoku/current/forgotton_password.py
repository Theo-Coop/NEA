from tkinter import *
from tkinter import messagebox
import smtplib
import random
import re
import bcrypt
import sql_commands



with open("email.txt") as f: # Get the email password from the text file that it is stored in. No point storing one key in a whole database table
    email_pw = f.read()


my_email = "theopythontesting@gmail.com" # Email address used for sending forgotton password emails
db = sql_commands.Sql() # creating an instance of the Sql class so I can execute queries using the classes' functions



# Template window so other windows can inherit reused code such as close function, and the self.FONT constant
class PasswordTemplateWindows:
    def __init__(self):
        self.window = Toplevel()
        self.FONT = ("Arial", 12, "bold")


    def close(self):
        self.window.destroy()




# Forgotton password class
class ForgottonPassword(PasswordTemplateWindows):
    def __init__(self):
        super().__init__()
        self.window.title("Forgotton password")
        

        self.email_label = Label(self.window, text="Enter your email", font=("Arial", 15, "bold"))
        self.email_label.grid(row=0, column=0, columnspan=3)

        self.email_entry = Entry(self.window, width=40)
        self.email_entry.grid(row=1, column=0, columnspan=3, padx=20, pady=10)


        self.return_but = Button(self.window, text="Return", command=self.close)
        self.return_but.grid(row=3, column=0, padx=10, pady=10)

        self.forgotton_password_button = Button(self.window, text="Send Code", font=self.FONT, command=self.send_email)
        self.forgotton_password_button.grid(row=3, column=1, padx=10, pady=10)


    def validate_email(self):
        self.entered_email = self.email_entry.get()

        return db.check_email(self.entered_email) == 1 # Make sure there is already this email address in the database


    def send_email_code(self, code): # The actual emailing, takes code as input so the user can request the code again
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection: # saves having to do connection.close()
                connection.starttls()
                connection.login(user=my_email, password=email_pw)
                connection.sendmail(from_addr=my_email, 
                    to_addrs=self.entered_email,
                    msg=f"Subject: Password code\n\nHello there. Your code is: {code}."
                )
        except:
            return False # If the email cannot be sent for any reason
        else:
            return True

        


    def send_email(self): # Function to generate the code and call the emailing function
        self.random_code = random.randint(100000, 999999) # Random code to be emailed to the user

        if self.validate_email(): # If the email is already in the DB
            if self.send_email_code(self.random_code): # Store the email sending code in another function so I can call it to resend email
                self.close() 
                CheckCode(self, self.random_code, self.entered_email) # if email sent successfully, close this window and open the CheckCode class
            else:
                messagebox.showerror(title="Error", message="An issue prevented the email being sent, either the email cannot be reached or there is a connection issue.")
        else:
            messagebox.showerror(title="Error", message="Email does not exist.")


    


# CheckCode class
class CheckCode(PasswordTemplateWindows):
    def __init__(self, window, code, entered_email):
        super().__init__()
        self.forgotton_pw_window = window # Takes in the old window's "self" so functions in the ForgottonPassword class can be called
        self.emailed_code = code
        self.entered_email = entered_email

        self.window.title("Verify code")


        # Tkinter UI variables
        self.enter_code_label = Label(self.window, text="Enter the code sent to your email", font=self.FONT)
        self.enter_code_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.code_input = Entry(self.window, font=("Arial", 20, "bold"), width=7, justify="center")
        self.code_input.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.create_new_password_but = Button(self.window, text="Verify", font=self.FONT, command=self.verify_code)
        self.create_new_password_but.grid(row=2, column=1, pady=10)

        self.resend_but = Button(self.window, text="Resend email", font=("Arial", 10, "bold"), command=self.resend_email)
        self.resend_but.grid(row=2, column=0)



    # If the user wants to resend the code
    def resend_email(self):
        self.forgotton_pw_window.send_email_code(self.emailed_code)
    

    def verify_code(self):
        # check if code is correct
        try:
            inputted_code = int(self.code_input.get())
        except:
            messagebox.showerror(title="Error", message="Something went wrong. Please enter the numerical code that you were emailed")
        else:
            if inputted_code == self.emailed_code:
                messagebox.showinfo(title="Congratulations", message="Code is correct. Please enter a new password when prompted.")
                self.close()
                NewPassword(self.entered_email) # Open the NewPassword class so user can create a new password
            else:
                messagebox.showerror(title="Error", message="The codes do not match.")
        


# New password class
# Once the user has successully received the email and typed in the correct code
class NewPassword(PasswordTemplateWindows):
    def __init__(self, entered_email):
        super().__init__()

        self.entered_email = entered_email

        self.window.title("Create new password")


        # Tkinter UI variables
        self.create_new_pw_label = Label(self.window, text="Enter a new password", font=self.FONT)
        self.create_new_pw_label.grid(row=0, column=0, columnspan=2)

        self.password_entry = Entry(self.window, show="*", font=self.FONT, width=20) # Show="*" makes every character when typing in appear as an * so people cannot see what you're typing
        self.password_entry.grid(row=1, column=0, columnspan=2, padx=20)


        self.second_pw_label = Label(self.window, text="Re-enter Password", font=self.FONT)
        self.second_pw_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.password_reentry = Entry(self.window, show="*", font=self.FONT, width=20)
        self.password_reentry.grid(row=3, column=0, columnspan=2, padx=20)


        self.finish_but = Button(self.window, text="Submit", font=("Arial", 12, "bold"), command=self.update_db)
        self.finish_but.grid(row=4, column=0, columnspan=2, padx=10, pady=10)



    # Validate the password against the regex
    # This regex is different, because the prefix (?=.*?) means that there must be one or more of the following characters
    # This is needed, as you need one or more of capital letter, lowecase letters, numbers, and symbols for a strong password
    # so this was the regex that I came up with so the user needs one or more of everything, and at least 8 characters long
    def validate_password(self):
        self.user_password = self.password_entry.get()
        self.user_password_reentry = self.password_reentry.get()

        regex = re.compile(r'^(?=.*?[0-9])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[#?!@$%^&*_-]).{8,}$')
        if regex.fullmatch(self.user_password):
            if self.user_password == self.user_password_reentry:
                return True
            else:
                messagebox.showerror(title="Error", message="Passwords do not match.")
        else:
            messagebox.showerror(title="Error", message="Please enter a valid password at least 8 characters long")


    # Hash the password
    # .encode() converts a string to "Bytes" format which is the data type needed for the hashing function to work
    def hash_pw(self):
        salt = bcrypt.gensalt() # Create the salt

        # hash the password
        hashed_pw = bcrypt.hashpw(self.user_password.encode(), salt)

        self.hashed_pw = hashed_pw.decode() # Turn it back into a string


    def update_db(self):
        if self.validate_password():
            # Hash PW
            self.hash_pw()

            # update DB
            db.update_password(self.entered_email, self.hashed_pw)
            
            messagebox.showinfo(title="Success", message="Congratulations, new password has been saved.")

            # Return to main program
            self.close()


