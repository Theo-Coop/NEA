from tkinter import *
from board import Board
from stack import Node, Stack

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
        clear_but.grid(row=0, column=1)

        undo_but = Button(self.window, text="Undo", font=FONT, command=self.undo)
        undo_but.grid(row=0, column=2)

        valid_but = Button(self.window, text="Valid", font=FONT, command=self.is_valid)
        valid_but.grid(row=0, column=3)

        for row in range(1, 10):
            for col in range(1, 10):

                if row in (1,2,3,7,8,9) and col in (4,5,6) or row in (4,5,6) and col in (1,2,3,7,8,9):
                    colour = "#FF99D7"
                else:
                    colour = "#FFD372"
                    

                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row+1, column=col)

                start_text = self.board.get_num(row, col)
                if start_text == 0:
                    game_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, foreground="red", font=FONT, command=lambda row=row, col=col: self.update_num(row, col))
                    game_buttons.pack()
                    self.game_button_dict[(row, col)] = game_buttons

                else:
                    starting_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, text=start_text, font=FONT, command=lambda row=row, col=col: self.update_num(row, col))
                    starting_buttons.pack()
                    starting_buttons["state"] = DISABLED
                    self.starting_button_dict[(row, col)] = game_buttons
                    

        empty_space = Label(self.window, text="")
        empty_space.grid(row=11, column=1)

        for i in range(1, 10):
            num_button = Button(self.window, width=4, height=2, padx=0, pady=0, text=i, font=FONT, command=lambda i=i: self.set_selected_num(i))
            num_button.grid(row=12, column=i)
            # lambda i=i means: it stores the value of i at the time your lambda is defined, instead of waiting to look up the value of i later when it will be equal to 9 every time.

            self.num_button_dict[i] = num_button


        self.window.mainloop()


    def set_selected_num(self, num):
        self.selected_num = num


    def get_selected_num(self): # Can probably delete this
        return self.selected_num


    def update_num(self, row, col):
        num = self.get_selected_num()
        self.board.update(num, row, col)
        self.game_button_dict[(row, col)].config(text=num)

        self.numbers_stack.push([(row,col), num])
 

    def undo(self):
        row, col = self.numbers_stack.pop()[0]
        self.board.reset_value(row, col)
        self.game_button_dict[(row, col)].config(text="")


    def is_valid(self):
        print(self.board.whole_board_valid())


    def clear(self):
        for button in self.game_button_dict:
            self.game_button_dict[button].config(text="")

        self.board.board_clear()

 
if __name__ == "__main__":
    Gui()