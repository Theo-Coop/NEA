from tkinter import *


class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sudoku")

        self.game_button_dict = {}
        self.starting_button_dict = {}
        self.num_button_dict = {}

        self.board = Board()
        

        for row in range(1, 10):
            for column in range(1, 10):

                if row in (1,2,3,7,8,9) and column in (4,5,6) or row in (4,5,6) and column in (1,2,3,7,8,9):
                    colour = "#FF99D7"
                else:
                    colour = "#FFD372"
                    

                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row, column=column)

                # cell = Entry(frame, justify="center", width=2, font=("Arial", 20))
                # cell.pack()

                # Still unsure whether to use buttons or text-entries
                start_text = self.board.get_num(row, column)
                if start_text == 0:
                    game_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, foreground="red", font=("Arial", 12, "bold"), command=lambda row=row, col=column: self.update_num(row, col))
                    game_buttons.pack()
                    self.game_button_dict[(row, column)] = game_buttons

                else:
                    starting_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, text=start_text, font=("Arial", 12, "bold"), command=lambda row=row, col=column: self.update_num(row, col))
                    starting_buttons.pack()
                    starting_buttons["state"] = DISABLED
                    self.starting_button_dict[(row, column)] = game_buttons
                    

        empty_space = Label(self.window, text="")
        empty_space.grid(row=10, column=1)

        for i in range(1, 10):
            num_button = Button(self.window, width=4, height=2, padx=0, pady=0, text=i, font=("Arial", 12, "bold"), command=lambda i=i: self.set_selected_num(i))
            num_button.grid(row=11, column=i)
            # lambda i=i means: it stores the value of i at the time your lambda is defined, instead of waiting to look up the value of i later when it will be equal to 9 every time.

            self.num_button_dict[i] = num_button


        self.window.mainloop()

    def set_selected_num(self, num):
        self.selected_num = num

    def get_selected_num(self):
        return self.selected_num

    def update_num(self, row, col):
        num = self.get_selected_num()
        self.board.update(num, row, col)
        self.game_button_dict[(row, col)].config(text=num)


class Board:
    def __init__(self):
        self.board = [
                    [0,7,5,0,0,0,0,1,6],
                    [2,0,0,3,0,0,0,0,0],
                    [0,0,0,0,0,1,7,0,2],
                    [0,2,3,1,0,0,4,0,0],
                    [0,0,0,0,0,7,0,6,0],
                    [7,0,9,4,0,5,0,0,0],
                    [5,3,8,0,1,4,9,0,7],
                    [1,0,7,0,2,8,6,3,4],
                    [0,0,0,0,9,3,0,5,0]
                        ]
            
    def update(self, num, y, x):
        self.board[y-1][x-1] = num

    
    def get_num(self, y, x):
        return self.board[y-1][x-1]



 
if __name__ == "__main__":
    Gui()