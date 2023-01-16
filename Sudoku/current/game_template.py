from tkinter import *
from tkinter import messagebox
import board_class_file
import stack


# This is the template class for the "free play" and "new game" modes
class GameTemplate:
    def __init__(self):
        self.window = Toplevel()

        self.FONT = ("Arial", 12, "bold") # Sets the default font constant
        self.BUTTON_BG_COLOUR = "#f0f0f0"

        # dictionaries so all certain buttons can be activated / deactivated / modified
        self.cells_dict = {}
        self.nums_dict = {}
        self.utilities_dict = {}

        # creates an instance of the "GameBoard" class to use its methods to modify the board
        self.board_class = board_class_file.GameBoard()

        # Create a stack using my "Stack" class
        self.numbers_stack = stack.Stack()


        # Draws the board
        for row in range(9):
            for col in range(9):
                # To get the colours in the correct places and make the board look like it is in 3x3 "boxes"
                if row in (0,1,2,6,7,8) and col in (3,4,5) or row in (3,4,5) and col in (0,1,2,6,7,8):
                    colour = "#6DB7CA"
                else:
                    colour = "#6163D3" # outisde - you want darker on the outside 
                

                # create a tkinter frame to store the buttons in
                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row, column=col)

                # Creates the game buttons
                # The lambda function allows the rows and columns to be stored in the dictionary as well (refer to line 54)
                game_buttons = Button(frame, justify="center", width=4, height=2, padx=0, pady=0, foreground="blue", bg=self.BUTTON_BG_COLOUR, font=self.FONT, command=lambda row=row, col=col: self.player_update_num(row, col))
                game_buttons.pack()
                self.cells_dict[(row, col)] = game_buttons

                
        # Empty space between game buttons and the numbers at the bottom of the board
        empty_space = Label(self.window, text="")
        empty_space.grid(row=10, column=1)


        # Create the numbers that the user uses to select their number
        for i in range(1,10):
            num_button = Button(self.window, width=4, height=2, padx=0, pady=0, text=i, font=self.FONT, command=lambda i=i: self.set_selected_num(i))
            num_button.grid(row=11, column=i-1)
            self.nums_dict[i-1] = num_button
            # lambda i=i means: it stores the value of i at the time the lambda is defined, instead of waiting to look up the value of i later when it will be equal to 9 every time.


        # A button to clear a single button on the cell
        single_button_clear = Button(self.window, width=4, height=2, padx=0, pady=0, text="Erase", font=self.FONT, command=lambda: self.set_selected_num(0))
        single_button_clear.grid(row=11, column=9, columnspan=2)
        self.nums_dict[9] = single_button_clear


    # Set the users selected number
    def set_selected_num(self, num):
        self.selected_num = num


    # A function that is called when the users trys to update a button on the board
    def player_update_num(self, row, col):
        # Checks if there is a selected number and throws an error if user has not selected a number
        try:
            num = self.selected_num
        except:
            messagebox.showerror(title="Number Error", message="Please select a number before trying to place a number")
        else:
            self.board_class.update(num, row, col) # Update the actual board (not the GUI)

            if num != 0: # If the button is not the "clear" button
                if self.board_class.num_valid(num, row, col): # If the number is actually valid
                    bg_colour = self.BUTTON_BG_COLOUR
                    fg_colour = "blue"
                else:
                    bg_colour = "red"
                    fg_colour = "white"

                self.cells_dict[(row, col)].config(text=num, foreground=fg_colour, bg=bg_colour, disabledforeground="blue", font=self.FONT)

                self.numbers_stack.push([(row,col), num]) # Push the number onto the stack

                if self.board_class.is_board_full() and self.board_class.whole_board_valid(): # If the board is completed and fully valid
                    messagebox.showinfo(title="Congratulations!", message="Congratulations, you have completed the puzzle!")


            else: # If the button is the "clear" button, put empty text on the game grid
                self.cells_dict[(row, col)].config(text="", bg=self.BUTTON_BG_COLOUR, foreground="blue", disabledforeground="blue", font=self.FONT)


    # Quit the program
    def quit(self):
        exit()


    # Close the current window
    def close(self):
        self.window.destroy()


    # Undo function
    def undo(self):
        # Checks if the user has placed a number because the stack cannot pop something if it is empty if the user hasn't placed any numbers
        try:
            row, col = self.numbers_stack.pop()[0]
        except:
            messagebox.showerror(title="Undo Error", message="You have not placed anything that you can undo")
        else:
            self.board_class.reset_value(row, col) # Reset the actual board's value
            self.cells_dict[(row, col)].config(text="", bg=self.BUTTON_BG_COLOUR)  # Update the GUI


    # Function to be used after the computer has solved the board so user cannot edit the board
    def disable_num_buttons(self):
        for button in self.nums_dict:
            self.nums_dict[button]["state"] = DISABLED

        self.selected_num = None


    # Function to enable the player to edit the board
    def enable_num_buttons(self):
        for button in self.nums_dict:
            self.nums_dict[button]["state"] = NORMAL


    # Function to disable the "utilities" buttons when solving is taking place
    def disable_utilities(self):
        for button in self.utilities_dict:
            self.utilities_dict[button]["state"] = DISABLED

        self.disable_num_buttons() # Disables the number buttons as well


    # Function to enable the "utilities" buttons when solving is finished
    def enable_utilities(self):
        for button in self.utilities_dict:
            self.utilities_dict[button]["state"] = NORMAL

        self.enable_num_buttons() # Enables the number buttons as well


    # Funciton to disable all the game cells when solving is taking place
    def disable_game_cells(self):
        for cell in self.cells_dict:
            self.cells_dict[cell]["state"] = DISABLED


    # Function to enable all the game cells when solving is finished
    def enable_game_cells(self):
        for cell in self.cells_dict:
            self.cells_dict[cell]["state"] = NORMAL


if __name__ == "__main__": # Just running on its own
    GameTemplate()