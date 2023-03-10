from tkinter import *

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

        self.forgotton_password_button = Button(self.window, text="Send Code", font=self.FONT, command=self.email_code)
        self.forgotton_password_button.grid(row=3, column=1, padx=10, pady=10)

        self.window.mainloop()


    def email_code(self):
        # Send email
        CheckCode(self)



class CheckCode(PasswordTemplateWindows):
    def __init__(self, window):
        super().__init__()
        self.forgotton_pw_window = window
        self.window.title("Verify code")


        self.enter_code_label = Label(self.window, text="Enter the code sent to your email", font=self.FONT)
        self.enter_code_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.code_input = Entry(self.window, font=("Arial", 20, "bold"), width=7, justify="center")
        self.code_input.grid(row=1, column=1, padx=10, pady=10)

        self.create_new_password_but = Button(self.window, text="Create new password", font=("Arial", 10, "bold"), command=self.verify_code)
        self.create_new_password_but.grid(row=2, column=1, pady=10)


    
    def verify_code(self):
        # check if code is correct
        self.close()
        self.forgotton_pw_window.close()
        NewPassword()
        


class NewPassword(PasswordTemplateWindows):
    def __init__(self):
        super().__init__()

        self.window.title("Create new password")


        self.create_new_pw_label = Label(self.window, text="Enter a new password", font=self.FONT)
        self.create_new_pw_label.grid(row=0, column=0, columnspan=2)

        self.password_entry = Entry(self.window, show="*", font=self.FONT, width=20)
        self.password_entry.grid(row=1, column=0, columnspan=2, padx=20)


        self.second_pw_label = Label(self.window, text="Re-enter Password", font=self.FONT)
        self.second_pw_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.password_reentry = Entry(self.window, show="*", font=self.FONT, width=20)
        self.password_reentry.grid(row=3, column=0, columnspan=2, padx=20)


        self.finish_but = Button(self.window, text="Submit", font=("Arial", 12, "bold"))
        self.finish_but.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.window.mainloop()


if __name__ == "__main__":
    ForgottonPassword()