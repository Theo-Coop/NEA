from tkinter import *


class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sudoku")

        for row in range(1, 10):
            for column in range(1, 10):

                if row in (1,2,3,7,8,9) and column in (4,5,6) or row in (4,5,6) and column in (1,2,3,7,8,9):
                    colour = "red"
                else:
                    colour = "blue"

                frame = Frame(self.window, width=10, height=10, padx=5, pady=5, bg=colour)
                frame.grid(row=row, column=column)

                # cell = Entry(frame, justify="center", width=2, font=("Arial", 20))
                # cell.pack()

                # Still unsure whether to use buttons or text-entries

                button = Button(frame, justify="center", width=4, height=2)
                button.pack()

        for i in range(1, 10):
            new_button = Button(self.window, width=4, height=2, text=i)
            new_button.grid(row=10, column=i)

        self.window.mainloop()

if __name__ == "__main__":
    Gui()