from tkinter import *
from tkinter import messagebox
import smtplib
import random
import re
import bcrypt
import sql_commands



with open("email.txt") as f: # Get the email password from the text file that it is stored in. Could use SQL but i really cbf rn.
    email_pw = f.read()


my_email = "theopythontesting@gmail.com"
db = sql_commands.Sql()


# class TempHiddenWindow:
#     def __init__(self):
#         self.window = Tk()
#         self.window.withdraw()

#         ForgottonPassword()

#         self.window.mainloop()


class PasswordTemplateWindows:
    def __init__(self):
        self.window = Toplevel()
        self.FONT = ("Arial", 12, "bold")


    def close(self):
        self.window.destroy()



class ForgottonPassword(PasswordTemplateWindows):
    def __init__(self):
        super().__init__()
        self.window.title("Forgotton password")
        

        self.email_label = Label(self.window, text="Enter your email", font=("Arial", 15, "bold"))
        self.email_label.grid(row=0, column=0, columnspan=3)

        self.email_entry = Entry(self.window, width=40)
        self.email_entry.grid(row=1, column=0, columnspan=3, padx=20, pady=10)


        self.return_but = Button(self.window, text="Return")
        self.return_but.grid(row=3, column=0, padx=10, pady=10)

        self.forgotton_password_button = Button(self.window, text="Send Code", font=self.FONT, command=self.send_email)
        self.forgotton_password_button.grid(row=3, column=1, padx=10, pady=10)


    def validate_email(self):
        self.entered_email = self.email_entry.get()

        if db.check_email(self.entered_email) == 1:
            return True
        else:
            return False


    def send_email_code(self, code): # The actual emailing, takes code as input so the user can request the code again
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection: # saves having to do connection.close()
                connection.starttls()
                connection.login(user=my_email, password=email_pw)
                print("sending...")
                connection.sendmail(from_addr=my_email, 
                    to_addrs=self.entered_email,
                    msg=f"Subject: Password code\n\nHello there. Your code is: {code}."
                )
        except:
            messagebox.showerror(title="Error", message="An issue prevented the email being sent, either the email cannot be reached or there is a connection issue.")
        else:
            messagebox.showinfo(title="Sent", message="Email has been sent")

        print(code)

    def send_email(self): # Function to generate the code and call the emailing function
        self.random_code = random.randint(100000, 999999)

        if self.validate_email(): # If the email is already in the DB
            self.send_email_code(self.random_code) # Store the email sending code in another function so I can call it to resend email
            self.close()
            CheckCode(self, self.random_code, self.entered_email)
        else:
            messagebox.showerror(title="Error", message="Email does not exist.")


    


class CheckCode(PasswordTemplateWindows):
    def __init__(self, window, code, entered_email):
        super().__init__()
        self.forgotton_pw_window = window
        self.emailed_code = code
        self.entered_email = entered_email

        self.window.title("Verify code")


        self.enter_code_label = Label(self.window, text="Enter the code sent to your email", font=self.FONT)
        self.enter_code_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.code_input = Entry(self.window, font=("Arial", 20, "bold"), width=7, justify="center")
        self.code_input.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.create_new_password_but = Button(self.window, text="Verify", font=self.FONT, command=self.verify_code)
        self.create_new_password_but.grid(row=2, column=1, pady=10)

        self.resend_but = Button(self.window, text="Resend email", font=("Arial", 10, "bold"), command=self.resend_email)
        self.resend_but.grid(row=2, column=0)




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
                NewPassword(self.entered_email)
            else:
                messagebox.showerror(title="Error", message="The codes do not match.")
        


class NewPassword(PasswordTemplateWindows):
    def __init__(self, entered_email):
        super().__init__()

        self.entered_email = entered_email

        self.window.title("Create new password")


        self.create_new_pw_label = Label(self.window, text="Enter a new password", font=self.FONT)
        self.create_new_pw_label.grid(row=0, column=0, columnspan=2)

        self.password_entry = Entry(self.window, show="*", font=self.FONT, width=20)
        self.password_entry.grid(row=1, column=0, columnspan=2, padx=20)


        self.second_pw_label = Label(self.window, text="Re-enter Password", font=self.FONT)
        self.second_pw_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.password_reentry = Entry(self.window, show="*", font=self.FONT, width=20)
        self.password_reentry.grid(row=3, column=0, columnspan=2, padx=20)


        self.finish_but = Button(self.window, text="Submit", font=("Arial", 12, "bold"), command=self.update_db)
        self.finish_but.grid(row=4, column=0, columnspan=2, padx=10, pady=10)



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


    def hash_pw(self):
        salt = bcrypt.gensalt() # Create the salt

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



# if __name__ == "__main__":
#     TempHiddenWindow()