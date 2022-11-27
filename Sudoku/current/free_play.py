from tkinter import *
from tkinter import messagebox
import windows
import board
import stack
import time


class FreePlayWindow(windows.WindowTemplate):
    def __init__(self):
        super().__init__()

        self.FONT = ("Arial", 12, "bold")

        self.cells_dict = {}
        self.nums_dict = {}
        self.utilities_dict = {}
        self.solving_speed = 0 # Default value

        
        self.board = board.FreePlayBoard()
        self.numbers_stack = stack.Stack()

        self.return_but = Button(self.window, text="Return", font=self.FONT, command=self.welcome_page)
        self.return_but.grid(row=0, column=0, columnspan=2)
        self.utilities_dict["return"] = self.return_but

        self.quit_but = Button(self.window, text="Quit", font=self.FONT, command=self.quit)
        self.quit_but.grid(row=0, column=2)
        self.utilities_dict["quit"] = self.quit_but

        self.wipe_but = Button(self.window, text="Wipe", font=self.FONT, command=self.wipe)
        self.wipe_but.grid(row=0, column=3)
        self.utilities_dict["wipe"] = self.wipe_but

        self.undo_but = Button(self.window, text="Undo", font=self.FONT, command=self.undo)
        self.undo_but.grid(row=0, column=4)
        self.utilities_dict["undo"] = self.undo_but

        self.solve_but = Button(self.window, text="Solve", font=self.FONT, command=self.solve)
        self.solve_but.grid(row=0, column=5)
        self.utilities_dict["solve"] = self.solve_but

        self.slider_val = DoubleVar()
        self.speed_slider = Scale(self.window, from_=0, to=100, orient="horizontal", command=self.slider_changed, variable=self.slider_val)
        self.speed_slider.grid(row=0, column=6, columnspan=3)
        self.disable_slider()
        

        for row in range(9):
            for col in range(9):

                if row in (0,1,2,6,7,8) and col in (3,4,5) or row in (3,4,5) and col in (0,1,2,6,7,8):
                    colour = "#FCE38A"
                else:
                    colour = "#FF75A0" # outisde - you want darker on the outside 
                    

                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row+1, column=col)


                game_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, foreground="blue", font=self.FONT, command=lambda row=row, col=col: self.player_update_num(row, col))
                game_buttons.pack()
                self.cells_dict[(row, col)] = game_buttons
                

        empty_space = Label(self.window, text="")
        empty_space.grid(row=11, column=1)

        for i in range(1,10):
            num_button = Button(self.window, width=4, height=2, padx=0, pady=0, text=i, font=self.FONT, command=lambda i=i: self.set_selected_num(i))
            num_button.grid(row=12, column=i-1)
            self.nums_dict[i] = num_button
            # lambda i=i means: it stores the value of i at the time your lambda is defined, instead of waiting to look up the value of i later when it will be equal to 9 every time.


    def welcome_page(self):
        self.close()
        windows.Welcome()

        
    def set_selected_num(self, num):
        self.selected_num = num

    
    def slider_changed(self, event):
        self.solving_speed = self.slider_val.get() / 1000


    def player_update_num(self, row, col):
        try:
            num = self.selected_num
        except:
            messagebox.showerror(title="Number Error", message="Please select a number before trying to place a number")
        else:
            self.board.update(num, row, col)
            self.cells_dict[(row, col)].config(text=num, foreground="blue", disabledforeground="blue", font=self.FONT)

            self.numbers_stack.push([(row,col), num])


    def wipe(self):
        self.board.new_board()
        
        self.enable_num_buttons()
        self.enable_game_cells()
        
        for cell in self.cells_dict:
            self.cells_dict[cell].config(text="")

        # Clears stack when the board is cleared
        self.numbers_stack.clear_stack()


    def undo(self):
        try:
            row, col = self.numbers_stack.pop()[0]
        except:
            messagebox.showerror(title="Undo Error", message="You have not placed anything that you can undo")
        else:
            self.board.reset_value(row, col)
            self.cells_dict[(row, col)].config(text="") 

    
    def solver_update_num(self, num, row, col, colour):
        self.cells_dict[(row, col)].config(text=num, disabledforeground=colour, font=self.FONT)


    def disable_num_buttons(self):  # Use this after computer has solved board so user cannot edit the board
        for i in range(1, 10):
            self.nums_dict[i]["state"] = DISABLED

        self.selected_num = None

    
    def enable_num_buttons(self):
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

    
    def disable_slider(self):
        self.speed_slider["state"] = DISABLED

    
    def enable_slider(self):
        self.speed_slider["state"] = NORMAL



    def solve(self):
        if self.board.whole_board_valid():
            self.numbers_stack.clear_stack()
            self.disable_game_cells()
            self.disable_utilities()
            self.enable_slider()

            find = self.board.find_empty()

            if find == False:
                # Solver has finished
                self.enable_utilities()
                self.enable_slider()
                return True
            else:
                row, col = find[0], find[1]

            for i in range(1, 10):
                if self.board.num_valid(i, row, col):
                    self.board.board[row][col] = i

                    self.window.update()
                    if self.solving_speed != 0:
                        time.sleep(self.solving_speed)
                    self.solver_update_num(i, row, col, "green")


                    if self.solve():
                        return True
                    else:
                        self.board.board[row][col] = 0

                        self.window.update()
                        self.solver_update_num("-", row, col, "red")
        else:
            messagebox.showerror(title="Error", message="Sorry, the current board is unsolvable")
                        

        return False