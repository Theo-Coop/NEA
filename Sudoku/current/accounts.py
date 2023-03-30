import re
import bcrypt
from tkinter import *
from tkinter import messagebox
import sql_commands
import forgotton_password


# So I can call SQL functions from the Sql class
db = sql_commands.Sql()


# Used so I do not have to keep repeating code such as creating a Toplevel, and the font etc.
class UserWindowsTemplate:
    def __init__(self):
        self.window = Toplevel()
        self.FONT = ("Arial", 12, "bold")


    # Close the window
    def close(self):
        self.window.destroy()


    # This function is used in both classes and they both have a "game_window" variable. 
    # This is used to return to the game without signing in / creating an account
    def go_back(self):
        self.game_window.show_window()
        self.close()



class SignIn(UserWindowsTemplate):
    def __init__(self, game_window): # Receives the current gamewindow so this class can show it when the user is done with the sign in
        # When called in the other class, it passes in "self" so this class can call functions in the other class when it is done.
        super().__init__() 
        self.window.title("Sign in")
        self.game_window = game_window


        # Tkinter UI variables
        self.username_label = Label(self.window, text="Username:", font=self.FONT)
        self.username_label.grid(row=0, column=0, padx=5)

        self.username_input = Entry(self.window, font=("Arial", 12))
        self.username_input.grid(row=0, column=1, padx=10, pady=10, columnspan=2)


        self.password_label = Label(self.window, text="Password:", font=self.FONT)
        self.password_label.grid(row=1, column=0)

        self.password_entry = Entry(self.window, show="*", font=self.FONT)
        self.password_entry.grid(row=1, column=1, columnspan=2)

        
        self.sign_in_but = Button(self.window, text="Sign in", font=self.FONT, command=self.check_inputs)
        self.sign_in_but.grid(row=2, column=0)

        self.create_account_but = Button(self.window, text="Create account", font=self.FONT, command=self.create_account)
        self.create_account_but.grid(row=2, column=1, pady=10)


        self.return_but = Button(self.window, text="Return", font=("Arial", 10), command=self.go_back)
        self.return_but.grid(row=3, column=0, pady=10)

        self.forgot_pw = Button(self.window, text="Forgot Password", font=("Arial", 10), command=self.forgotton_pw)
        self.forgot_pw.grid(row=3, column=1)


    # Check that both entries have text
    def check_inputs(self):
        if self.username_input.get() and self.password_entry.get(): # If the user actually inputted text
            self.sign_in()
        else:
            messagebox.showerror(title="Error", message="Please enter text in all fields before continuing") 



    def sign_in(self):
        # Sign in logic
        self.inputted_username = self.username_input.get()
        self.inputted_password = self.password_entry.get().encode() # Have to convert the password from "string", to "bytes" format for the Bcrypt algorithm

        try: # Check if there is a user account with the username supplied
            pre_existing_hash = (db.return_password(self.inputted_username)).encode()
        except:
            messagebox.showerror(title="Error", message="There is no user with that Username.")
        else:
            if bcrypt.checkpw(self.inputted_password, pre_existing_hash): # If the password's match
                self.game_window.show_window() # Shows the hidden window
                self.game_window.signed_in(self.inputted_username) # Calls the function in the "New Game" file
                self.close() # Close this window
            else:
                messagebox.showerror(title="Error", message="Username or Password is not valid.") # Otherwise, user has entered something wrong
    

    # Calls the ForgottonPassword class
    def forgotton_pw(self):
        forgotton_password.ForgottonPassword()


    # Calls the CreateAccount class
    def create_account(self):
        CreateAccount(self.game_window)
        self.close()




# CreateAccount class
class CreateAccount(UserWindowsTemplate):
    def __init__(self, game_window): # Takes in the "self" from the NewGame class, so it can call functions in that file to go back
        super().__init__()
        self.window.title("Create an account")
        self.game_window = game_window

        
        # Tkinter UI variables
        self.email_label = Label(self.window, text="Email:", font=self.FONT)
        self.email_label.grid(row=0, column=0, padx=5)

        self.email_input = Entry(self.window, font=("Arial", 10), width=40)
        self.email_input.grid(row=0, column=1, columnspan=2, padx=10)


        self.username_label = Label(self.window, text="Username:", font=self.FONT)
        self.username_label.grid(row=1, column=0, padx=5)

        self.username_input = Entry(self.window, font=("Arial", 12), width=31)
        self.username_input.grid(row=1, column=1, padx=10, pady=10, columnspan=2)


        self.password_label = Label(self.window, text="Password:", font=self.FONT)
        self.password_label.grid(row=2, column=0)

        self.password_entry = Entry(self.window, show="*", font=self.FONT, width=31)
        self.password_entry.grid(row=2, column=1, columnspan=2)


        self.second_pw_label = Label(self.window, text="Re-enter Password:", font=self.FONT)
        self.second_pw_label.grid(row=3, column=0, padx=10, pady=10)

        self.password_reentry = Entry(self.window, show="*", font=self.FONT, width=31) # show="*" makes the password show up as ** whatver the user types
        self.password_reentry.grid(row=3, column=1, columnspan=2)


        self.password_info_button = Button(self.window, text="Password requirements", font=("Arial", 10), command=self.password_requirements_popup)
        self.password_info_button.grid(row=4, column=0)


        self.create_password_button = Button(self.window, text="Create!", font=("Arial", 13, "bold"), command=self.check_inputs, padx=20)
        self.create_password_button.grid(row=4, column=1, pady=10)

        self.return_but = Button(self.window, text="Return", font=("Arial", 10), command=self.go_back)
        self.return_but.grid(row=4, column=2, pady=10)


    # Pop-up to show the user the password requirements
    def password_requirements_popup(self):
        messagebox.showinfo(title="Password requirements", message=("Please create a strong password, which is at least "
                                                                    "8 characters long, using a combination of capital "
                                                                    "and lowercase letters, numbers, and symbols.\n"
                                                                    "Symbols accepted: #?!@$%^&*-\n"
                                                                    "You must use at least one of everything mentioned."))


    # Return True if all the inputs are filled in and False if not
    def all_inputs_filled(self):
        return self.email_input.get() and self.username_input.get() and self.password_entry.get() and self.password_reentry.get()


    # Validates the entered email against the regular expression, to see if it is a valid email address
    def validate_email(self):
        user_email = self.email_input.get()

        regex = re.compile(r'^[a-zA-Z0-9_.+-]+[@][a-zA-Z0-9-]+[.][a-zA-Z0-9-.]+$')
        if regex.fullmatch(user_email):
            return True
        else:
            messagebox.showerror(title="Error", message="Please enter a valid email address")

    
    # Validate the username against regex checking that there are only letters, numbers, and '_.-'
    def validate_username(self):
        user_username = self.username_input.get()

        
        if db.check_username(user_username) == 1: # If the username already exists
            messagebox.showerror(title="Error", message="Username already taken")
        else:
            regex = re.compile(r'^[a-zA-Z0-9_.-]+$')
            if regex.fullmatch(user_username):
                return True
            else:
                messagebox.showerror(title="Error", message=("Please enter a username only containing upper and "
                                                            "lowercase letters, numbers, and the characters: _.-"))
    

    # Validate the inputted password against the regex. 
    # This regex is different, because the prefix (?=.*?) means that there must be one or more of the following characters
    # This is needed, as you need one or more of capital letter, lowecase letters, numbers, and symbols for a strong password
    # so this was the regex that I came up with so the user needs one or more of everything, and at least 8 characters long
    def validate_password(self):
        user_password = self.password_entry.get()
        user_password_reentry = self.password_reentry.get()

        regex = re.compile(r'^(?=.*?[0-9])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[#?!@$%^&*_-]).{8,}$')
        if regex.fullmatch(user_password):
            if user_password == user_password_reentry: # checks both passwords entered are the same
                return True
            else:
                messagebox.showerror(title="Error", message="Passwords do not match.")
        else:
            messagebox.showerror(title="Error", message="Please enter a valid password at least 8 characters long")


    # Make sure every input is valid
    def check_inputs(self):
        if self.all_inputs_filled():
            if self.validate_email() and self.validate_username() and self.validate_password():
                self.create_account()
        else:
            messagebox.showerror(title="Error", message="Please enter text in all fields before continuing")


    # The user has now created an account
    def create_account(self):
        messagebox.showinfo(title="Congratulations!", message="You have successfully created an account!")    
       
        # Create account
        self.email = self.email_input.get()
        self.username = self.username_input.get()
        self.password = self.password_entry.get().encode() # make it "bytes" format for hashing

        salt = bcrypt.gensalt() # Create the salt

        hashed_pw = bcrypt.hashpw(self.password, salt) # Hash the password
        hashed_pw = hashed_pw.decode() # Turn it back into a string to put it in the database

        db.add_user(self.username, self.email, hashed_pw) # Insert username, email, hashed password into the database


        # Call the SignIn class so the user can sign into their account now they've created one
        SignIn(self.game_window)
        self.close() # Close this window