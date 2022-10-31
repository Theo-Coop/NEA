from tkinter import *

class Windows:
    def __init__(self):
        self.root = Tk()
        self.root.title("Hello")
        self.label = Label(self.root, text="This is the first page").pack()
        self.but = Button(self.root, text="click or else", command=self.new_window).pack()

        self.root.mainloop()

    def new_window(self):
        self.root.destroy()
        self.window = Tk()
        self.window.title("Page 2 easy")
        self.new_label = Label(self.window, text="This is page 2").pack()


if __name__ == "__main__":
    Windows()