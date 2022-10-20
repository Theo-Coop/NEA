from tkinter import *
from tkinter import messagebox
from board import Board
from stack import Stack

FONT = ("Arial", 12, "bold")


class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sudoku")

        self.game_button_dict = {}
        self.starting_button_dict = {}
        self.num_button_dict = {}

        self.board = Board()
        self.numbers_stack = Stack()


        clear_but = Button(self.window, text="Clear", font=FONT, command=self.clear)
        clear_but.grid(row=0, column=0)

        undo_but = Button(self.window, text="Undo", font=FONT, command=self.undo)
        undo_but.grid(row=0, column=1)

        valid_but = Button(self.window, text="Valid", font=FONT, command=self.is_valid)
        valid_but.grid(row=0, column=2)

        for row in range(9):
            for col in range(9):

                if row in (0,1,2,6,7,8) and col in (3,4,5) or row in (3,4,5) and col in (0,1,2,6,7,8):
                    colour = "#94DAFF"
                else:
                    colour = "#94B3FD" # outisde - you want darker on the outside 
                    

                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row+1, column=col)

                start_text = self.board.get_num(row, col)
                if start_text == 0:
                    game_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, foreground="red", font=FONT, command=lambda row=row, col=col: self.update_num(row, col))
                    game_buttons.pack()
                    self.game_button_dict[(row, col)] = game_buttons

                else:
                    starting_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, text=start_text, font=FONT)
                    starting_buttons.pack()
                    starting_buttons["state"] = DISABLED
                    self.starting_button_dict[(row, col)] = game_buttons
                    

        empty_space = Label(self.window, text="")
        empty_space.grid(row=11, column=1)

        for i in range(1,10):
            num_button = Button(self.window, width=4, height=2, padx=0, pady=0, text=i, font=FONT, command=lambda i=i: self.set_selected_num(i))
            num_button.grid(row=12, column=i-1)
            # lambda i=i means: it stores the value of i at the time your lambda is defined, instead of waiting to look up the value of i later when it will be equal to 9 every time.

            self.num_button_dict[i] = num_button


        self.window.mainloop()


    def set_selected_num(self, num):
        self.selected_num = num


    def get_selected_num(self): # Can probably delete this
        return self.selected_num


    def update_num(self, row, col):
        try:
            num = self.get_selected_num()
        except:
            messagebox.showerror(title="Number Error", message="Please select a number before trying to place a number")
        else:
            self.board.update(num, row, col)
            self.game_button_dict[(row, col)].config(text=num)

            self.numbers_stack.push([(row,col), num])
 

    def undo(self):
        try:
            row, col = self.numbers_stack.pop()[0]
        except:
            messagebox.showerror(title="Undo Error", message="You have not placed anything that you can undo")
        else:
            self.board.reset_value(row, col)
            self.game_button_dict[(row, col)].config(text="")


    def is_valid(self):
        print(self.board.whole_board_valid())


    def clear(self):
        for button in self.game_button_dict:
            self.game_button_dict[button].config(text="")

        self.board.board_clear()
        
        # Clears stack when the board is cleared
        while not self.numbers_stack.is_empty():
            self.numbers_stack.pop()

 
if __name__ == "__main__":
    Gui()