from tkinter import *
from tkinter import messagebox
from copy import deepcopy
import windows
import game_template
import generate_board
import accounts


generateBoardClass = generate_board.GenerateBoard() # Create an instance of the GeneratedBoard class

# Select Difficulty window
class SelectDifficuly:
    def __init__(self):
        self.window = Toplevel() # Create a new Tkinter window

        self.FONT = ("Arial", 15, "bold") # Set the window font size

        self.window.title("Select difficulty") # Set the window title

        # Difficulty buttons which call the set_difficulty() function
        self.easy_but = Button(self.window, text="Easy", font=self.FONT, width=8, command=lambda: self.set_difficulty("easy")).place(x=45, y=5)
        self.medium_but = Button(self.window, text="Medium", font=self.FONT, width=8, command=lambda: self.set_difficulty("medium")).place(x=45, y=55)
        self.hard_but = Button(self.window, text="Hard", font=self.FONT, width=8, command=lambda: self.set_difficulty("hard")).place(x=45, y=105)

        # Return button
        self.return_but = Button(self.window, text="Return", font=("Arial", 12, "bold"), width=8, command=self.welcome_page).place(x=52, y=155)

    
    # Close the window
    def close(self):
        self.window.destroy()

    # Return to the welcome page
    def welcome_page(self):
        self.close()
        windows.Welcome()

    # Call the NewGame class with the desired difficulty
    def set_difficulty(self, difficulty):
        self.close()
        NewGame(difficulty)



# NewGame window
class NewGame(game_template.GameTemplate):
    def __init__(self, difficulty):
        super().__init__() # Inherits from the GameTemplate class

        self.lives = 5 # Number of lives the user has
        self.INCORRECT_ICON = "❌"

        self.window.title(f"New Game - {difficulty.capitalize()} difficulty") # Sets the window title
        
        # A constant which is the starting board generated from the GenerateBoard class in generate_board.py
        self.STARTING_BOARD = generateBoardClass.create_board(difficulty)

        # Testing starting board
        # self.STARTING_BOARD = [
        #     [1,2,3,4,5,6,0,0,0],
        #     [7,8,9,1,2,3,4,5,6],
        #     [4,5,6,7,8,9,1,2,3],
        #     [3,4,5,6,7,8,9,1,2],
        #     [9,1,2,3,4,5,6,7,8],
        #     [6,7,8,9,1,2,3,4,5],
        #     [5,6,7,8,9,1,2,3,4],
        #     [2,3,4,5,6,7,8,9,1],
        #     [8,9,1,2,3,4,5,6,7]
        # ]


        self.board_class.game_board = deepcopy(self.STARTING_BOARD)       # Changes the game_board variable in the GameBoard class in the "board_class_file.py"

        self.populate_board() # Populate the board with numbers


        # Buttons
        self.sign_in_button = Button(self.window, text="Sign in", font=self.FONT, command=self.sign_in)
        self.sign_in_button.grid(row=0, column=11)
        
        self.create_account_button = Button(self.window, text="Create account", font=self.FONT, command=self.create_account)
        self.create_account_button.grid(row=0, column=12, columnspan=2, padx=10)

        
        self.game_options_label = Label(self.window, text="Game options", font=self.FONT)
        self.game_options_label.grid(row=1, column=11, columnspan=3)

        self.clear_but = Button(self.window, text="Clear", font=self.FONT, padx=10, command=self.clear)
        self.clear_but.grid(row=2, column=11)

        self.undo_but = Button(self.window, text="Undo", font=self.FONT, padx=10, command=self.undo)
        self.undo_but.grid(row=2, column=12, columnspan=2, padx=10)


        self.return_label = Label(self.window, text="Return options", font=self.FONT)
        self.return_label.grid(row=4, column=11, columnspan=3)

        self.quit_but = Button(self.window, text="Quit", font=self.FONT, padx=10, command=self.quit)
        self.quit_but.grid(row=5, column=11, padx=10)


        self.return_but = Button(self.window, text="Return", font=self.FONT, padx=10, command=self.select_diffficulty)
        self.return_but.grid(row=5, column=12, columnspan=2)

        # "Incorrect guesses" text
        self.return_label = Label(self.window, text="Incorrect guesses", font=self.FONT)
        self.return_label.grid(row=7, column=11, columnspan=3)

        self.incorrect_guesses_label = Label(self.window, text=f"", fg="red", font=self.FONT)
        self.incorrect_guesses_label.grid(row=8, column=11, columnspan=3)


    def sign_in(self):
        self.window.withdraw()
        accounts.SignIn(self.window) # Passing in the actual window into the sign in class so I can show the window again

    
    def create_account(self):
        self.window.withdraw()
        accounts.CreateAccount(self.window)


    # Function to close the window and return to the select difficulty page
    def select_diffficulty(self):
        self.close()
        SelectDifficuly()

    
    # Clears only the user's inputs
    def clear(self):
        for row in range(9):
            for column in range(9):
                if (row, column) not in self.generated_buttons_dict:
                    self.cells_dict[(row, column)].config(text="", bg=self.BUTTON_BG_COLOUR) # Clears the GUI board's numbers

        self.board_class.clear_user_inputs(self.STARTING_BOARD) # Uses the board_class "clear user inputs" function to clear the backend board of the user's numbers
        
        # Clears stack when the board is cleared
        self.numbers_stack.clear_stack()

    
    # Wipes entire board
    def wipe(self):
        self.generated_buttons_dict = {} # Reset the buttons dictionary

        self.numbers_stack.clear_stack() # Clear the stack

        for button in self.cells_dict:
            self.cells_dict[button].config(text="", bg=self.BUTTON_BG_COLOUR) # Make all the buttons have no text
            self.cells_dict[button]["state"] = NORMAL # Make the buttons able to be pressed

    
    # Function to populate the board with the numbers from the generated sudoku
    def populate_board(self):
        self.wipe()
        for row in range(9):
            for col in range(9):
                num = self.STARTING_BOARD[row][col]
                if num != 0:
                    self.generated_buttons_dict[(row, col)] = self.cells_dict[(row, col)]
                    self.generated_buttons_dict[(row, col)].config(text=num) # Put the number on the board
                    self.generated_buttons_dict[(row, col)]["state"] = DISABLED # Disable the starting numbers buttons so the user cannot overwrite them


    # A function that is called when the users trys to update a button on the board
    def player_update_num(self, row, col):
        # Checks if there is a selected number and throws an error if user has not selected a number
        try:
            num = self.selected_num
        except:
            messagebox.showerror(title="Number Error", message="Please select a number before trying to place a number")
        else:
            # self.board_class.update(num, row, col) # Update the backend board (not the GUI)
            if num != 0: # If the button is not the "clear" button
                if self.board_class.num_valid(num, row, col): # If the number is actually valid
                    self.cells_dict[(row, col)].config(text=num, foreground="blue", bg=self.BUTTON_BG_COLOUR, font=self.FONT)

                else: # If the user inputted number is incorrect according to the rules of Sudoku
                    self.cells_dict[(row, col)].config(text=num, foreground="white", bg="red", font=self.FONT)
                    
                    new_text = self.incorrect_guesses_label.cget("text") + "❌"
                    self.incorrect_guesses_label.config(text=new_text)

                    self.lives -= 1 # Decrease the user's lives each time they place a wrong value

                    if self.lives == 0:
                        messagebox.showerror(title="You lose!", message="You have used all 5 of your lives, you lose!")
                        self.close()
                        SelectDifficuly()

                existing_num = self.board_class.return_num(row, col)

                if existing_num != 0: # There is already a number in that spot on the board
                    if num != existing_num: # If the user has overwritten the already placed number with a new number
                        self.board_class.update(num, row, col)
                        self.numbers_stack.remove_element((row, col)) # Remove the old number from the stack
                        self.numbers_stack.push([(row,col), num])
                else:
                    self.board_class.update(num, row, col)
                    self.numbers_stack.push([(row,col), num])

                
                if self.board_class.is_board_full() and self.board_class.whole_board_valid(): # If the board is completed and fully valid
                    messagebox.showinfo(title="Congratulations!", message="Congratulations, you have completed the puzzle!")


            else: # If the button is the "clear" button, put empty text on the game grid
                self.cells_dict[(row, col)].config(text="", bg=self.BUTTON_BG_COLOUR, foreground="blue", disabledforeground="blue", font=self.FONT)
                self.numbers_stack.remove_element((row, col))