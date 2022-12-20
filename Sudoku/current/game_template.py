from tkinter import *
from tkinter import messagebox
import board_class_file
import stack

class gameTemplate:
    def __init__(self):
        self.window = Toplevel()

        self.FONT = ("Arial", 12, "bold")

        self.cells_dict = {}
        self.nums_dict = {}
        self.utilities_dict = {}

        self.board_class = board_class_file.GameBoard()
        self.numbers_stack = stack.Stack()


        for row in range(9):
            for col in range(9):

                if row in (0,1,2,6,7,8) and col in (3,4,5) or row in (3,4,5) and col in (0,1,2,6,7,8):
                    colour = "#FCE38A"
                else:
                    colour = "#FF75A0" # outisde - you want darker on the outside 
                    

                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row, column=col)


                game_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, foreground="blue", font=self.FONT, command=lambda row=row, col=col: self.player_update_num(row, col))
                game_buttons.pack()
                self.cells_dict[(row, col)] = game_buttons
                

        empty_space = Label(self.window, text="")
        empty_space.grid(row=10, column=1)

        for i in range(1,10):
            num_button = Button(self.window, width=4, height=2, padx=0, pady=0, text=i, font=self.FONT, command=lambda i=i: self.set_selected_num(i))
            num_button.grid(row=11, column=i-1)
            self.nums_dict[i] = num_button
            # lambda i=i means: it stores the value of i at the time your lambda is defined, instead of waiting to look up the value of i later when it will be equal to 9 every time.

        num_button = Button(self.window, width=4, height=2, padx=0, pady=0, font=self.FONT, command=lambda: self.set_selected_num(0))
        num_button.grid(row=11, column=9)
        self.nums_dict[10] = num_button


    def set_selected_num(self, num):
        self.selected_num = num


    def player_update_num(self, row, col):
        try:
            num = self.selected_num
        except:
            messagebox.showerror(title="Number Error", message="Please select a number before trying to place a number")
        else:
            self.board_class.update(num, row, col)
            if num != 0: # If the button is not the "clear" button
                self.cells_dict[(row, col)].config(text=num, foreground="blue", disabledforeground="blue", font=self.FONT)
                self.numbers_stack.push([(row,col), num])

            else: # If the button is the "clear" button, put empty text on the game grid
                self.cells_dict[(row, col)].config(text="", foreground="blue", disabledforeground="blue", font=self.FONT)




    def undo(self):
        try:
            row, col = self.numbers_stack.pop()[0]
        except:
            messagebox.showerror(title="Undo Error", message="You have not placed anything that you can undo")
        else:
            self.board_class.reset_value(row, col)
            self.cells_dict[(row, col)].config(text="") 


    def disable_num_buttons(self):  # Use this after computer has solved board so user cannot edit the board
        for i in range(1, 10):
            self.nums_dict[i]["state"] = DISABLED

        self.selected_num = None


    def enable_num_buttons(self):          # Use this so the player can edit the board
        for button in self.nums_dict:
            self.nums_dict[button]["state"] = NORMAL


    def disable_utilities(self):    # Use this to disable the "utilities" buttons when solving is taking place
        for button in self.utilities_dict:
            self.utilities_dict[button]["state"] = DISABLED

        self.disable_num_buttons()


    def enable_utilities(self):    # Use this to enable the "utilities" buttons when solving is finished
        for button in self.utilities_dict:
            self.utilities_dict[button]["state"] = NORMAL

        self.enable_num_buttons()


    def disable_game_cells(self): # Use this to disable all the game cells when solving is taking place
        for cell in self.cells_dict:
            self.cells_dict[cell]["state"] = DISABLED


    def enable_game_cells(self): # Use this to enable all the game cells when solving is finished
        for cell in self.cells_dict:
            self.cells_dict[cell]["state"] = NORMAL


if __name__ == "__main__": # Just running on its own
    gameTemplate()