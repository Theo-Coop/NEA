from tkinter import *


class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sudoku")

        self.button_dict = {}
        self.num_button_dict = {}

        for column in range(1, 10):
            for row in range(1, 10):

                if row in (1,2,3,7,8,9) and column in (4,5,6) or row in (4,5,6) and column in (1,2,3,7,8,9):
                    colour = "#757070"
                else:
                    colour = "#969494"
                    

                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row, column=column)

                # cell = Entry(frame, justify="center", width=2, font=("Arial", 20))
                # cell.pack()

                # Still unsure whether to use buttons or text-entries

                button = Button(frame, justify="center", width=4, height=2)
                button.pack()

                self.button_dict[(column, row)] = button

        for i in range(1, 10):
            num_button = Button(self.window, width=4, height=2, text=i, command=lambda: self.update_buttons(i))
            num_button.grid(row=10, column=i)

            self.num_button_dict[i] = num_button

        print(self.button_dict)

        self.window.mainloop()

    def update_buttons(self, num):
        print(num)

if __name__ == "__main__":
    Gui()