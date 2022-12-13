from tkinter import *
from tkinter import messagebox
import time
import game_template
import windows

class freePlayWindow(game_template.gameTemplate):
    def __init__(self):
        super().__init__()

        self.window.title("Free Play")

        self.solving_speed = 0 # Default value

        
        self.grid_10 = Label(self.window, text="      ")
        self.grid_10.grid(row=0, column=10)

        self.solve_label = Label(self.window, text="Solve options", font=self.FONT)
        self.solve_label.grid(row=0, column=11, columnspan=3)

        self.solve_but = Button(self.window, text="Solve", font=self.FONT, command=self.solve)
        self.solve_but.grid(row=1, column=11)
        self.utilities_dict["solve"] = self.solve_but

        self.instant_solve_but = Button(self.window, text="Instant Solve", font=self.FONT, command=self.instant_solve)
        self.instant_solve_but.grid(row=1, column=12, padx=20, columnspan=2)
        self.utilities_dict["instant-solve"] = self.instant_solve_but


        self.slider_text = Label(self.window, text="Delay Slider:", font=self.FONT)
        self.slider_text.grid(row=2, column=11, columnspan=2)

        self.slider_val = DoubleVar()
        self.speed_slider = Scale(self.window, from_=0, to=100, showvalue=0, orient="horizontal", command=self.slider_changed, variable=self.slider_val)
        self.speed_slider.grid(row=2, column=13, columnspan=2)
        self.disable_slider()


        self.game_options_label = Label(self.window, text="Game options", font=self.FONT)
        self.game_options_label.grid(row=4, column=11, columnspan=3)

        self.wipe_but = Button(self.window, text="Wipe", font=self.FONT, padx=10, command=self.wipe)
        self.wipe_but.grid(row=5, column=11)
        self.utilities_dict["wipe"] = self.wipe_but

        self.undo_but = Button(self.window, text="Undo", font=self.FONT, padx=10, command=self.undo)
        self.undo_but.grid(row=5, column=12, columnspan=2)
        self.utilities_dict["undo"] = self.undo_but


        self.return_label = Label(self.window, text="Return options", font=self.FONT)
        self.return_label.grid(row=7, column=11, columnspan=3)

        self.quit_but = Button(self.window, text="Quit", font=self.FONT, padx=10, command=self.quit)
        self.quit_but.grid(row=8, column=11, padx=10)
        self.utilities_dict["quit"] = self.quit_but

        self.return_but = Button(self.window, text="Return", font=self.FONT, padx=10, command=self.welcome_page)
        self.return_but.grid(row=8, column=12, columnspan=2)
        self.utilities_dict["return"] = self.return_but




    def quit(self):
        exit()

    
    def close(self):
        self.window.destroy()


    def welcome_page(self):
        self.close()
        windows.Welcome()

    
    def slider_changed(self, event):
        self.solving_speed = self.slider_val.get() / 1000


    def wipe(self):
        self.board.new_board()
        
        self.enable_num_buttons()
        self.enable_game_cells()
        
        for cell in self.cells_dict:
            self.cells_dict[cell].config(text="")

        # Clears stack when the board is cleared
        self.numbers_stack.clear_stack()

    
    def solver_update_num(self, num, row, col, colour):
        self.cells_dict[(row, col)].config(text=num, disabledforeground=colour, fg=colour, font=self.FONT)

    
    def disable_slider(self):
        self.speed_slider["state"] = DISABLED

    
    def enable_slider(self):
        self.speed_slider["state"] = NORMAL


    def instant_solve(self):
        if self.board.whole_board_valid():
            self.numbers_stack.clear_stack()
            self.board.instant_solve()

            for row in range(9):
                for col in range(9):
                    if self.cells_dict[(row, col)]["text"] == "":
                        num = self.board.board[row][col]
                        self.solver_update_num(num, row, col, "green")

        else:
            messagebox.showerror(title="Error", message="Sorry, the current board is unsolvable")

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

                        # self.window.update()
                        self.solver_update_num("-", row, col, "red")
        else:
            messagebox.showerror(title="Error", message="Sorry, the current board is unsolvable")
                        

        return False