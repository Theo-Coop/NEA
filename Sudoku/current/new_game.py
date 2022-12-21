from tkinter import *
from copy import deepcopy
import windows
import game_template
import generate_board


class SelectDifficuly:
    def __init__(self):
        self.window = Toplevel()

        self.FONT = ("Arial", 15, "bold")

        self.window.title("Select difficulty")

        self.easy_but = Button(self.window, text="Easy", font=self.FONT, width=8, command=lambda: self.set_difficulty("easy")).place(x=45, y=5)
        self.medium_but = Button(self.window, text="Medium", font=self.FONT, width=8, command=lambda: self.set_difficulty("medium")).place(x=45, y=55)
        self.hard_but = Button(self.window, text="Hard", font=self.FONT, width=8, command=lambda: self.set_difficulty("hard")).place(x=45, y=105)

        self.return_but = Button(self.window, text="Return", font=("Arial", 12, "bold"), width=8, command=self.welcome_page).place(x=52, y=155)

    
    def close(self):
        self.window.destroy()

    def welcome_page(self):
        self.close()
        windows.Welcome()

    def set_difficulty(self, difficulty):
        self.close()
        NewGame(difficulty)




class NewGame(game_template.gameTemplate):
    def __init__(self, difficulty):
        super().__init__()
        self.STARTING_BOARD = generate_board.GenerateBoard(difficulty).starting_board     # A constant which is the starting board generated from the GenerateBoard class in generate_board.py


        self.board_class.game_board = deepcopy(self.STARTING_BOARD)       # Changes the game_board variable in the GameBoard class in the board_class_file.py

        self.populate_board()

        # Buttons
        self.game_options_label = Label(self.window, text="Game options", font=self.FONT)
        self.game_options_label.grid(row=0, column=11, columnspan=3)

        self.clear_but = Button(self.window, text="Clear", font=self.FONT, padx=10, command=self.clear)
        self.clear_but.grid(row=1, column=11)
        self.utilities_dict["clear"] = self.clear_but

        self.undo_but = Button(self.window, text="Undo", font=self.FONT, padx=10, command=self.undo)
        self.undo_but.grid(row=1, column=12, columnspan=2, padx=10)
        self.utilities_dict["undo"] = self.undo_but


        self.return_label = Label(self.window, text="Return options", font=self.FONT)
        self.return_label.grid(row=3, column=11, columnspan=3)

        self.quit_but = Button(self.window, text="Quit", font=self.FONT, padx=10, command=self.quit)
        self.quit_but.grid(row=4, column=11, padx=10)
        self.utilities_dict["quit"] = self.quit_but

        self.return_but = Button(self.window, text="Return", font=self.FONT, padx=10, command=self.select_diffficulty)
        self.return_but.grid(row=4, column=12, columnspan=2)
        self.utilities_dict["return"] = self.return_but


    def select_diffficulty(self):
        self.close()
        SelectDifficuly()

    
    # Clears only the user's inputs
    def clear(self):
        for row in range(9):
            for column in range(9):
                if (row, column) not in self.generated_buttons_dict:
                    self.cells_dict[(row, column)].config(text="")

        self.board_class.clear_user_inputs(self.STARTING_BOARD)
        
        # Clears stack when the board is cleared
        self.numbers_stack.clear_stack()

    
    # Wipes entire board
    def wipe(self):
        self.generated_buttons_dict = {}

        self.numbers_stack.clear_stack()

        for button in self.cells_dict:
            self.cells_dict[button].config(text="")
            self.cells_dict[button]["state"] = NORMAL


    def populate_board(self):
        self.wipe()
        for row in range(9):
            for col in range(9):
                num = self.STARTING_BOARD[row][col]
                if num != 0:
                    self.generated_buttons_dict[(row, col)] = self.cells_dict[(row, col)]
                    self.generated_buttons_dict[(row, col)].config(text=num)
                    self.generated_buttons_dict[(row, col)]["state"] = DISABLED