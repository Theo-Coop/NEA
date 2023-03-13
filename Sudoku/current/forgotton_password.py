from tkinter import *
from tkinter import messagebox
import smtplib


with open("email.txt") as f: # Get the email password from the text file that it is stored in. Could use SQL but i really cbf rn.
    email_pw = f.read()


my_email = "theopythontesting@gmail.com"


class TempHiddenWindow:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        ForgottonPassword()

        self.window.mainloop()


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

        self.forgotton_password_button = Button(self.window, text="Send Code", font=self.FONT, command=self.initialise_email)
        self.forgotton_password_button.grid(row=3, column=1, padx=10, pady=10)



    def initialise_email(self):
        self.send_email()
        self.close()
        CheckCode(self)


    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection: # saves having to do connection.close()
            connection.starttls()
            connection.login(user=my_email, password=email_pw)
            print("sending...")
            connection.sendmail(from_addr=my_email, 
                to_addrs="theomantelcooper@gmail.com",
                msg="Subject: Password code\n\nHello there. Your code is: 567891."
            )

        messagebox.showinfo(title="Sent", message="Email has been sent")



class CheckCode(PasswordTemplateWindows):
    def __init__(self, window):
        super().__init__()
        self.forgotton_pw_window = window
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
        self.forgotton_pw_window.send_email()
    

    def verify_code(self):
        # check if code is correct
        messagebox.showinfo(title="Congratulations", message="Code is correct. Please enter a new password when prompted.")
        self.close()
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



if __name__ == "__main__":
    TempHiddenWindow()