from tkinter import *
from tkinter import messagebox
import time
import game_template
import windows

# The Class for the "Free Play" mode which inherits from the GameTemplte class
class FreePlayWindow(game_template.GameTemplate):
    def __init__(self):
        super().__init__()

        self.window.title("Free Play") # Sets the windows title

        self.solving_speed = 0 # Default value

        # Don't need if "clear" button is there
        # self.grid_10_blank_space = Label(self.window, text="      ")
        # self.grid_10_blank_space.grid(row=0, column=10)

        # Text which says "Solve options"
        self.solve_label = Label(self.window, text="Solve options", font=self.FONT)
        self.solve_label.grid(row=0, column=11, columnspan=3)

        # The "Solve" button which is then added to the "utilities_dict"
        self.solve_but = Button(self.window, text="Solve", font=self.FONT, command=self.solve)
        self.solve_but.grid(row=1, column=11)
        self.utilities_dict["solve"] = self.solve_but

        # The "Instant Solve" button which is added to the "utilities_dict"
        self.instant_solve_but = Button(self.window, text="Instant Solve", font=self.FONT, command=self.instant_solve)
        self.instant_solve_but.grid(row=1, column=12, padx=20, columnspan=2)
        self.utilities_dict["instant-solve"] = self.instant_solve_but

        # The Delay Slider text
        self.slider_text = Label(self.window, text="Delay Slider:", font=self.FONT)
        self.slider_text.grid(row=2, column=11, columnspan=2)

        # The Delay Slider 
        self.slider_val = DoubleVar()
        self.speed_slider = Scale(self.window, from_=0, to=100, showvalue=0, orient="horizontal", command=self.slider_changed, variable=self.slider_val)
        self.speed_slider.grid(row=2, column=13, columnspan=2)
        self.disable_slider()  # Disables the slider when you open this window

        
        # Game options text
        self.game_options_label = Label(self.window, text="Game options", font=self.FONT)
        self.game_options_label.grid(row=4, column=11, columnspan=3)

        # Wipe button which is added to the "utilities_dict"
        self.wipe_but = Button(self.window, text="Wipe", font=self.FONT, padx=10, command=self.wipe)
        self.wipe_but.grid(row=5, column=11)
        self.utilities_dict["wipe"] = self.wipe_but

        # Undo button which is added to the "utilities_dict"
        self.undo_but = Button(self.window, text="Undo", font=self.FONT, padx=10, command=self.undo)
        self.undo_but.grid(row=5, column=12, columnspan=2)
        self.utilities_dict["undo"] = self.undo_but


        # "Return options" text
        self.return_label = Label(self.window, text="Return options", font=self.FONT)
        self.return_label.grid(row=7, column=11, columnspan=3)

        # Button used to quit the whole program which is added to the "utilities_dict"
        self.quit_but = Button(self.window, text="Quit", font=self.FONT, padx=10, command=self.quit)
        self.quit_but.grid(row=8, column=11, padx=10)
        self.utilities_dict["quit"] = self.quit_but

        # Button used to return to the Welcome Page which is added to the "utilities_dict"
        self.return_but = Button(self.window, text="Return", font=self.FONT, padx=10, command=self.welcome_page)
        self.return_but.grid(row=8, column=12, columnspan=2)
        self.utilities_dict["return"] = self.return_but


    # Close current window and call the "Welcome" class from the "windows.py"
    def welcome_page(self):
        self.close()
        windows.Welcome()

    
    # This is called if the slider value has changed, so "self.solving_speed" is updated with the new speed
    def slider_changed(self, event):
        self.solving_speed = self.slider_val.get() / 1000
         # Scale goes from 0-100 so divide by 1000 to get the accurate time.sleep sleep time

    
    # Updates the board cell buttons with the solver numbers
    def solver_update_num(self, num, row, col, colour):
        self.cells_dict[(row, col)].config(text=num, disabledforeground=colour, fg=colour, font=self.FONT)
        # Change the certain button to the new solver's updated button

    
    # Function to disable the slider
    def disable_slider(self):
        self.speed_slider["state"] = DISABLED

    
    # Function to enable the slider
    def enable_slider(self):
        self.speed_slider["state"] = NORMAL

    
    # A function that is called when the users trys to update a button on the board
    def player_update_num(self, row, col):
        # Checks if there is a selected number and throws an error if user has not selected a number
        try:
            num = self.selected_num
        except:
            messagebox.showerror(title="Number Error", message="Please select a number before trying to place a number")
        else:
            if num != 0: # If the button is not the "clear" button
                if self.board_class.num_valid(num, row, col): # If the number is actually valid
                    self.cells_dict[(row, col)].config(text=num, foreground="blue", disabledforeground="blue", bg=self.BUTTON_BG_COLOUR, font=self.FONT)
                else:
                    self.cells_dict[(row, col)].config(text=num, foreground="white", bg="red", font=self.FONT)


                existing_num = self.board_class.return_num(row, col)
        
                if existing_num != 0: # There is already a number in that spot on the board
                    if num != existing_num: # If the user has overwritten the already placed number with a new number
                        self.board_class.update(num, row, col)
                        self.numbers_stack.remove_element((row, col)) # Remove the old number from the stack
                        self.numbers_stack.push([(row,col), num])
                else:
                    self.board_class.update(num, row, col)
                    self.numbers_stack.push([(row,col), num]) # Push the number onto the stack

            else: # If the button is the "clear" button, put empty text on the game grid
                self.cells_dict[(row, col)].config(text="", foreground="blue", disabledforeground="blue", bg=self.BUTTON_BG_COLOUR)
                self.board_class.update(num, row, col)
                self.numbers_stack.remove_element((row, col))


    # Instant solve function
    def instant_solve(self):
        if self.board_class.whole_board_valid(): # checks if the board is valid first
            self.numbers_stack.clear_stack() # Clears the stack
            self.board_class.instant_solve() # Calls the instant solve in the "board_class_file.py"

            for row in range(9): # Updates every number with the solved numbers
                for col in range(9):
                    if self.cells_dict[(row, col)]["text"] == "":
                        num = self.board_class.return_num(row, col)
                        self.solver_update_num(num, row, col, "green")

        else:
            messagebox.showerror(title="Error", message="Sorry, the current board is unsolvable")
            # If board is unsolvable, throw an error to the user


    # Solve function
    def solve(self):
        if self.board_class.whole_board_valid(): # Checks if the board is valid first
            self.numbers_stack.clear_stack() # Clears the stack
            self.disable_game_cells() # Makes the cells disabled so user cannot press them
            self.disable_utilities() # Disables the utility buttons so user cannot press them
            self.enable_slider() # Enables the delay slider

            find = self.board_class.find_empty() # Find an empty square

            if find == False:
                # Solver has finished
                self.enable_utilities() # Enables utilities
                self.disable_slider() # Disables slider
                return True
            else:
                row, col = find[0], find[1]

            for i in range(1, 10):
                if self.board_class.num_valid(i, row, col): # Checks if the number is valid in that spot
                    self.board_class.update(i, row, col)

                    self.window.update() # Have to do this with Tkinter when using the "time" module
                    if self.solving_speed != 0:
                        time.sleep(self.solving_speed) # Put in a delay
                    self.solver_update_num(i, row, col, "green")


                    if self.solve(): # Recursive call of this function
                        return True
                    else:
                        # Otherwise, "backtrack" by placing a 0
                        self.board_class.update(0, row, col)

                        self.solver_update_num("-", row, col, "red") # Update the button with red to show backtracking
        else:
            messagebox.showerror(title="Error", message="Sorry, the current board is unsolvable")
            # Show the user an error if the board is unsolvable                         

        return False