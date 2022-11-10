from tkinter import *
import windows


class FreePlayWindow(windows.WindowTemplate):
    def __init__(self):
        super().__init__()
        self.FONT = ("Arial", 12, "bold")

        self.return_but = Button(self.window, text="Return", font=self.FONT, command=self.welcome_page).grid(row=0, column=0, columnspan=2)
        self.quit_but = Button(self.window, text="Quit", font=self.FONT, command=self.quit).grid(row=0, column=2)

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
                # self.all_cells_dict[(row, col)] = game_buttons
                

        empty_space = Label(self.window, text="")
        empty_space.grid(row=11, column=1)

        for i in range(1,10):
            num_button = Button(self.window, width=4, height=2, padx=0, pady=0, text=i, font=self.FONT, command=lambda i=i: self.set_selected_num(i))
            num_button.grid(row=12, column=i-1)
            # lambda i=i means: it stores the value of i at the time your lambda is defined, instead of waiting to look up the value of i later when it will be equal to 9 every time.


    def welcome_page(self):
        self.close()
        windows.Welcome()
        