from tkinter import *
import requests
import free_play
import new_game


class WindowTemplate:
    def __init__(self):
        self.window = Toplevel()

        self.FONT = ("Arial", 15, "bold")

    def close(self):
        self.window.destroy()

    def quit(self):
        exit()


class hidden:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()
        
        Welcome()
        self.window.mainloop()


class Welcome(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.window.title("Welcome!")
        self.window.geometry("225x200")

        self.new_game_but = Button(self.window, text="New game", font=self.FONT, width=10, command=self.open_new_game).place(x=45, y=5)
        self.free_play_but = Button(self.window, text="Free play", font=self.FONT, width=10, command=self.open_freeplay).place(x=45, y=55)
        self.rules_but = Button(self.window, text="How to play", font=self.FONT, width=10, command=self.open_rules).place(x=45, y=105)

        self.quit_but = Button(self.window, text="Quit", font=("Arial", 12, "bold"), width=8, command=self.quit).place(x=65, y=155)

    
    def open_rules(self):
        self.close()
        Rules()

    def open_freeplay(self):
        self.close()
        free_play.freePlayWindow()

    def open_new_game(self):
        self.close()
        new_game.SelectDifficuly()


class Rules(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.window.title("Rules of Sudoku")
        self.window.geometry("300x450")

        api_text = requests.get(url="https://api.npoint.io/683413d787a24bac2915").json()
        text = api_text["Sudoku"]["Rules"]

        self.label = Label(self.window, text=text, font=("Arial", 12, "bold"), wraplength=200).place(x=50, y=10)
        
        self.return_but = Button(self.window, text="Return", font=self.FONT, command=self.welcome_page).place(x=110, y=375)
        

    def welcome_page(self):
        Welcome()
        self.close()




if __name__ == "__main__":
    hidden()