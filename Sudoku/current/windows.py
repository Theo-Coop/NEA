from tkinter import *
import requests
import free_play
import new_game


# A template that the windows can inheret from that include close and quit functions, and the default font
class WindowTemplate:
    def __init__(self):
        self.window = Toplevel() # This creates a  new Tkinter window

        self.FONT = ("Arial", 15, "bold") # Default font

    # Just closes the current window
    def close(self):
        self.window.destroy()

    # Exits the whole program
    def quit(self):
        exit()


# Hidden window to run in the background because one window needs a "mainloop" and tkinter does not like
# windows constantly opening and closing each with their own mainloop so this windows is always open
# but hidden in the background
class hidden:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw() # Hides the window
        
        Welcome() # Calls the main Welcome class
        self.window.mainloop()


class Welcome(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.window.title("Welcome!")
        self.window.geometry("225x200") # Sets the size of the window

        # "New Game" button
        self.new_game_but = Button(self.window, text="New game", font=self.FONT, width=10, command=self.open_new_game).place(x=45, y=5)

        # "Free play" button
        self.free_play_but = Button(self.window, text="Free play", font=self.FONT, width=10, command=self.open_freeplay).place(x=45, y=55)

        # "Rules" Button
        self.rules_but = Button(self.window, text="How to play", font=self.FONT, width=10, command=self.open_rules).place(x=45, y=105)

        # Button to quit the program
        self.quit_but = Button(self.window, text="Quit", font=("Arial", 12, "bold"), width=8, command=self.quit).place(x=65, y=155)


    # Function to close the current window and open the rules page by calling the "Rules" class
    def open_rules(self):
        self.close()
        Rules()

    # Function to close the current window and open the FreePlayWindow class in the "free_play.py" file
    def open_freeplay(self):
        self.close()
        free_play.FreePlayWindow()

    # Function to close the current window and open the SelectDifficulty class in "new_game.py" file
    def open_new_game(self):
        self.close()
        new_game.SelectDifficuly()


# Calls my API which holds the data for the rules page
# This is outside the class because it only has to run once at the start of the program
# Instead of running every time the "Rules" page is opened which takes time
API_TEXT = requests.get(url="https://api.npoint.io/683413d787a24bac2915").json()
TEXT = API_TEXT["Sudoku"]["Rules"]  # Stores the text in a constant


# Rules page class
class Rules(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.window.title("Rules of Sudoku") # Sets the title of the window
        self.window.geometry("300x450") # Sets the size of the window

        
        # The text which has been collected from the API
        self.label = Label(self.window, text=TEXT, font=("Arial", 12, "bold"), wraplength=200).place(x=50, y=10)
        
        # A button so the user can return to the Welcome page
        self.return_but = Button(self.window, text="Return", font=self.FONT, command=self.welcome_page).place(x=110, y=375)
        

    # A function to close the current window and return to the original welcome page
    def welcome_page(self):
        Welcome()
        self.close()




if __name__ == "__main__":
    hidden()