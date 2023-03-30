from tkinter import *
from tkinter import messagebox
from copy import deepcopy
import json
import windows
import game_template
import generate_board
import accounts
import save_and_load
import sql_commands


generateBoardClass = generate_board.GenerateBoard() # Create an instance of the GeneratedBoard class
db = sql_commands.Sql()



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

        self.username = "" # When signed in, username is stored

        self.is_signed_in = False # Variable to store whether the user is signed in or not
        self.lives = 5 # Number of lives the user has
        self.INCORRECT_ICON = "❌"

        
        
        # A constant which is the starting board generated from the GenerateBoard class in generate_board.py
        self.STARTING_BOARD = generateBoardClass.create_board(difficulty)

        db_starting_board = json.dumps(deepcopy(self.STARTING_BOARD))
        self.puzzle_id = db.get_latest_puzzleid() + 1


        # Insert the starting board and difficulty into the database
        db.insert_into_puzzle(self.puzzle_id, db_starting_board, difficulty) 


        self.window.title(f"New Game - {difficulty.capitalize()} difficulty. Puzzle {self.puzzle_id}") # Sets the window title
        

        #  Changes the game_board variable in the GameBoard class in the "board_class_file.py"
        self.board_class.game_board = deepcopy(self.STARTING_BOARD)

        self.populate_board() # Populate the board with numbers


        # Buttons
        self.account_label = Label(self.window, text="", font=("Arial", 10)) # Account label for when user is signed in
        self.account_label.grid(row=0, column=12)
        
        self.create_sign_in_buttons() # creates sign in buttons

        
        self.game_options_label = Label(self.window, text="Game options", font=self.FONT)
        self.game_options_label.grid(row=1, column=11, columnspan=3)

        self.clear_but = Button(self.window, text="Clear", font=self.FONT, padx=10, command=self.clear)
        self.clear_but.grid(row=2, column=11)

        self.undo_but = Button(self.window, text="Undo", font=self.FONT, padx=10, command=self.undo)
        self.undo_but.grid(row=2, column=12, columnspan=2, padx=10)

        self.save_but = Button(self.window, text="Save", font=self.FONT, padx=10, command=self.save_puzzle)
        self.save_but.grid(row=3, column=11, padx=10)

        self.load_but = Button(self.window, text="Load", font=self.FONT, padx=10, command=self.load_puzzle)
        self.load_but.grid(row=3, column=12, columnspan=2, padx=10)


        self.load_previous_but = Button(self.window, text="Load pre-generated puzzles", font=("Arial", 10, "bold"), command=self.load_starting_board)
        self.load_previous_but.grid(row=4, column=11, columnspan=3, padx=10)


        self.return_label = Label(self.window, text="Return options", font=self.FONT)
        self.return_label.grid(row=5, column=11, columnspan=3)

        self.quit_but = Button(self.window, text="Quit", font=self.FONT, padx=10, command=self.quit)
        self.quit_but.grid(row=6, column=11, padx=10)


        self.return_but = Button(self.window, text="Return", font=self.FONT, padx=10, command=self.select_diffficulty)
        self.return_but.grid(row=6, column=12, columnspan=2)

        # "Incorrect guesses" text
        self.return_label = Label(self.window, text="Incorrect guesses", font=self.FONT)
        self.return_label.grid(row=7, column=11, columnspan=3)

        self.incorrect_guesses_label = Label(self.window, text=f"", fg="red", font=self.FONT)
        self.incorrect_guesses_label.grid(row=8, column=11, columnspan=3)


    # Save puzzle function
    def save_puzzle(self):
        if not self.is_signed_in: # If the person isn't signed in
            messagebox.showerror(title="Error", message="You must be signed into your account to save puzzles")
        else:
            edited_board_copy = deepcopy(self.board_class.game_board)
            save_and_load.SavePuzzle(self.username, self.puzzle_id, self.lives, edited_board_copy) # Call SavePuzzle class


    # Load puzzle function
    def load_puzzle(self):
        if not self.is_signed_in: # Person must be signed in
            messagebox.showerror(title="Error", message="You must be signed into your account to load puzzles")
        else:
            save_and_load.LoadPuzzle(self.username, self) # Call LoadPuzzle class (pass through "self", so functions in this class can be called from the LoadPuzzle class)

    
    # Repopulate a loaded puzzle (with user's edits)
    def repopulate_loaded_puzzle(self, lives, start_board, edited_board, saveid):
        self.STARTING_BOARD = json.loads(start_board)
        self.board_class.game_board = json.loads(edited_board).copy() # Json.loads converts a json string back into the original 2D list as it must be stored as a string in the DB
        self.lives = lives # Changes the number of lives to the number on the previous save
        
        self.populate_board() # Add the starting board numbers onto the board


        for row in range(9):
            for column in range(9):
                num = self.board_class.game_board[row][column] # grab the current number from the board
                
                if num != 0 and num != self.STARTING_BOARD[row][column]: # If the number is not 0 or not equal to a game square then place it as the user has edited it
                    if self.board_class.num_valid(num, row, column): # If the number is actually valid
                        self.cells_dict[(row, column)].config(text=num, foreground="blue", bg=self.BUTTON_BG_COLOUR, font=self.FONT)

                    else: # If the old inputted numbers were incorrect according to the rules of Sudoku
                        self.cells_dict[(row, column)].config(text=num, foreground="white", bg="red", font=self.FONT)
        

        # Change title to say loaded puzzle
        self.window.title(f"Loaded game - {saveid}")

        # Add the number of lives lost
        self.incorrect_guesses_label.config(text=self.INCORRECT_ICON*(5-lives)) # Put the number of incorrect guesses onto the screen


    # Load a starting board
    def load_starting_board(self):
        if not self.is_signed_in: # user must be signed in
            messagebox.showerror(title="Error", message="You must be signed into your account to load puzzles")
        else:
            save_and_load.LoadStartingBoard(self) # Call the LoadStartingBoard class and pass in "self"


    # Repopulate the starting board
    def repopulate_starting_board(self, start_board, puzzleid):
        self.STARTING_BOARD = json.loads(start_board) # Json.loads() to convert back to a 2D list
        self.board_class.game_board = deepcopy(self.STARTING_BOARD) # Make the game board equal to the starting board

        self.populate_board() # Wipes the board, clears stack, adds numbers to the board

        self.window.title(f"Playing loaded puzzle {puzzleid}")

        # Reset lives and incorrect guesses icon as user is starting a fresh game
        self.lives = 5
        self.incorrect_guesses_label.config(text="")



    # Shows the window
    def show_window(self):
        self.window.deiconify()

    
    # Create Tkinter sign in buttons
    def create_sign_in_buttons(self):
        self.sign_in_button = Button(self.window, text="Sign in", font=self.FONT, command=self.sign_in)
        self.sign_in_button.grid(row=0, column=11)

        self.create_account_button = Button(self.window, text="Create account", font=self.FONT, command=self.create_account)
        self.create_account_button.grid(row=0, column=12, columnspan=2, padx=10)


    def signed_in(self, username): # The user is now signed in
        self.username = username # Set the username variable to be the username of whoever is currently signed in

        self.is_signed_in = True
        self.create_account_button.destroy() # Remove the sign in and create account buttons, as user is signed in
        self.sign_in_button.destroy()

        self.sign_out_button = Button(self.window, text="Sign out", font=self.FONT, command=self.sign_out) # Create a sign out button
        self.sign_out_button.grid(row=0, column=11)


        self.account_label.config(text=f"Signed in as: {username}")


    def sign_out(self):
        self.sign_out_button.destroy() # Destroy the sign out button

        self.create_sign_in_buttons() # Re place the sign in buttons

        self.account_label.config(text="")

        self.is_signed_in = False


    def sign_in(self):
        self.window.withdraw() # Hide the window

        accounts.SignIn(self) # Passing in this instance into the sign in class so functions can be called from that class

    
    def create_account(self):
        self.window.withdraw() # Hide the window
        accounts.CreateAccount(self) # Pass in self


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
    # Polymorphism because overwriting the wipe() method in the game_template file
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
            if num != 0: # If the button is not the "clear" button
                if self.board_class.num_valid(num, row, col): # If the number is actually valid
                    self.cells_dict[(row, col)].config(text=num, foreground="blue", bg=self.BUTTON_BG_COLOUR, font=self.FONT)

                else: # If the user inputted number is incorrect according to the rules of Sudoku
                    self.cells_dict[(row, col)].config(text=num, foreground="white", bg="red", font=self.FONT)
                    
                    new_text = self.incorrect_guesses_label.cget("text") + "❌" # Add another "X" to the incorrect guesses label
                    self.incorrect_guesses_label.config(text=new_text)

                    self.lives -= 1 # Decrease the user's lives each time they place a wrong value

                    if self.lives == 0:
                        messagebox.showerror(title="You lose!", message="You have used all 5 of your lives, you lose!")
                        self.close()
                        SelectDifficuly() # Return to the select difficulty page if user has used all their lives

                existing_num = self.board_class.return_num(row, col) # What number is in the selected spot?

                if existing_num != 0: # There is already a number in that spot on the board
                    if num != existing_num: # If the user has overwritten the already placed number with a new number
                        self.board_class.update(num, row, col) # Update the backend board (not the GUI)
                        self.numbers_stack.remove_element((row, col)) # Remove the old number from the stack
                        self.numbers_stack.push([(row,col), num])
                else: # There is no current number on the board (it is 0)
                    self.board_class.update(num, row, col)
                    self.numbers_stack.push([(row,col), num]) # push to stack

                
                if self.board_class.is_board_full() and self.board_class.whole_board_valid(): # If the board is completed and fully valid
                    messagebox.showinfo(title="Congratulations!", message="Congratulations, you have completed the puzzle!")


            else: # If the button is the "clear" button, put empty text on the game grid
                self.cells_dict[(row, col)].config(text="", bg=self.BUTTON_BG_COLOUR, foreground="blue", disabledforeground="blue", font=self.FONT)
                self.numbers_stack.remove_element((row, col)) # Remove the element that is being cleared from the stack