from tkinter import *
import windows

class SelectDifficuly:
    def __init__(self):
        self.window = Toplevel()

        self.FONT = ("Arial", 15, "bold")

        self.window.title("Select difficulty")

        self.easy_but = Button(self.window, text="Easy", font=self.FONT, width=10, command=lambda: self.set_difficulty("easy")).place(x=45, y=5)
        self.medium_but = Button(self.window, text="Medium", font=self.FONT, width=10, command=lambda: self.set_difficulty("medium")).place(x=45, y=55)
        self.hard_but = Button(self.window, text="Hard", font=self.FONT, width=10, command=lambda: self.set_difficulty("hard")).place(x=45, y=105)

        self.return_but = Button(self.window, text="Return", font=("Arial", 12, "bold"), width=8, command=self.welcome_page).place(x=65, y=155)

    
    def close(self):
        self.window.destroy()

    def welcome_page(self):
        self.close()
        windows.Welcome()

    def set_difficulty(self, difficulty):
        self.close()
        NewGame(difficulty)


class NewGame:
    def __init__(self, difficulty):
        print(difficulty)

