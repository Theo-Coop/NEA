from tkinter import *
from tkinter import messagebox
import json
import random
import sql_commands



db = sql_commands.Sql() # Create an instance of the Database class 



class SavePuzzle:
    def __init__(self, username, puzzleid, edited_board):
        self.window = Toplevel()

        # Generate SaveID
        self.save_id = random.randint(1000, 9999) # Random 4 digit number
        while db.check_save_id(self.save_id) == 1: # While there is an already existing saveID the same as the just generated one
            self.save_id = random.randint(1000, 9999)

        self.username = username # The username of whoever is signed in
        self.puzzle_id = puzzleid
        self.edited_board = json.dumps(edited_board)

        self.window.title("Save Puzzle")
        self.FONT = ("Arial", 12, "bold")

        self.info_label = Label(self.window, text=f"Your Save ID is: {self.save_id}. Please note it down or remember it", font=self.FONT, wraplength=200)
        self.info_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.submit_but = Button(self.window, text="Submit", font=self.FONT, command=self.submit)
        self.submit_but.grid(row=1, column=1, pady=5)


    
    def close(self):
        self.window.destroy()


    def submit(self):
        # Get UserID of whoever is signed in
        user_id = db.get_user_id(self.username)

        # DB insert into save
        db.insert_into_save(self.save_id, user_id, self.puzzle_id, self.edited_board)

        messagebox.showinfo(title="Success", message="Board saved.")

        self.close()
    




class LoadPuzzle:
    def __init__(self, username, game_window):
        self.window = Toplevel()

        self.username = username
        self.game_window = game_window

        self.window.title("Load puzzle")
        self.FONT = ("Arial", 12, "bold")

        self.info_label = Label(self.window, text="Enter your unique Save ID:", font=self.FONT)
        self.info_label.grid(row=0, column=0, columnspan=3)

        self.load_entry = Entry(self.window, font=self.FONT)
        self.load_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.load_but = Button(self.window, text="Load", font=self.FONT, command=self.load)
        self.load_but.grid(row=2, column=1, pady=5)

        self.window.mainloop()


    def close(self):
        self.window.destroy()


    def load(self):
        saveid = self.load_entry.get()

        user_id = db.get_user_id(self.username)

        edited_puzzle = db.get_edited_board(user_id, saveid)

        

        self.close()


if __name__ == "__main__":
    LoadPuzzle("yes")