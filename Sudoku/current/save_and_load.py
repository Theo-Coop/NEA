import random
from tkinter import *
from tkinter import messagebox
import sql_commands



db = sql_commands.Sql() # Create an instance of the Database class 



class SavePuzzle:
    def __init__(self, username, starting_board, edited_board):
        self.window = Toplevel()

        self.username = username # The username of whoever is signed in
        self.starting_board = starting_board
        self.edited_board = edited_board

        self.window.title("Save Puzzle")
        self.FONT = ("Arial", 12, "bold")

        self.info_label = Label(self.window, text="Create a unique Save ID:", font=self.FONT)
        self.info_label.grid(row=0, column=0, columnspan=3)

        self.save_entry = Entry(self.window, font=self.FONT)
        self.save_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.submit_but = Button(self.window, text="Submit", font=self.FONT, command=self.submit)
        self.submit_but.grid(row=2, column=1, pady=5)

        self.window.mainloop()

    
    def close(self):
        self.window.destroy()


    def submit(self):
        user_save_id = self.save_entry.get()
        if " " in user_save_id or user_save_id == "": # Checks if input has spaces inside it or if it empty
            messagebox.showerror(title="Error", message="Save ID cannot have spaces in it or be empty")
        else:
            # Get UserID of whoever is signed in
            user_id = db.get_user_id(self.username)

            puzzle_id = str(user_id) + self.save_entry.get()

            # db.insert_into_puzzle(user_id, puzzle_id, self.starting_board, self.edited_board)
            

            messagebox.showinfo(title="Success", message="Board saved.")

            self.close()
        




class LoadPuzzle:
    def __init__(self):
        self.window = Toplevel()

        self.window.title("Load puzzle")
        self.FONT = ("Arial", 12, "bold")

        self.info_label = Label(self.window, text="Enter your unique Save ID:", font=self.FONT)
        self.info_label.grid(row=0, column=0, columnspan=3)

        self.load_entry = Entry(self.window, font=self.FONT)
        self.load_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.load_but = Button(self.window, text="Load", font=self.FONT)
        self.load_but.grid(row=2, column=1, pady=5)


        self.window.mainloop()


    # TODO
    def load(self):
        pass


if __name__ == "__main__":
    LoadPuzzle()