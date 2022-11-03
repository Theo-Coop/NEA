from tkinter import *


class WindowTemplate:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x500")

    
    def close(self):
        self.window.destroy()


class hidden(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.window.withdraw()
        
        Welcome()
        self.window.mainloop()


class Welcome(WindowTemplate):
    def __init__(self):
        super().__init__()
        FONT = ("Arial", 15, "bold")
        self.window.title("Welcome!")
        self.window.geometry("225x150")

        self.new_game_but = Button(self.window, text="New game", font=FONT, width=10).place(x=45, y=0)
        self.free_play_but = Button(self.window, text="Free play", font=FONT, width=10).place(x=45, y=50)
        self.rules_but = Button(self.window, text="How to play", font=FONT, width=10).place(x=45, y=100)





hidden()