from tkinter import *


FONT = ("Arial", 15, "bold")

class Window_Template:
    def __init__(self):
        self.root = Tk()
        self.root.title("easy peasy")
        self.root.geometry("250x250")
        self.label = Label(self.root, text="messi is the goat").pack()

        self.retun_but = Button(self.root, text="return", command=self.menu).pack()


    def menu(self):
        Welcome_Window()
        self.root.destroy()


class Welcome_Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Welcome!")
        self.root.geometry("250x150")

        self.new_game_but = Button(self.root, text="New Game", font=FONT, width=10, command=self.new_game_activation).place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.free_play_but = Button(self.root, text="Free Play", font=FONT, width=10, command=self.free_play_activation).place(relx=0.5, rely=0.5, anchor=CENTER)

        self.rules_but = Button(self.root, text="How to play", font=FONT, width=10, command=self.rules_activation).place(relx=0.5, rely=0.8, anchor=CENTER)

        self.root.mainloop()

    def new_game_activation(self):
        New_Game_Window()
        self.root.destroy()

    def free_play_activation(self):
        Free_Play_Window()
        self.root.destroy()

    def rules_activation(self):
        Rules_Window()
        self.root.destroy()


class New_Game_Window(Window_Template):
    def __init__(self):
        super().__init__()


class Free_Play_Window(Window_Template):
    def __init__(self):
        super().__init__()


class Rules_Window(Window_Template):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    Welcome_Window()