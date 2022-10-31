from tkinter import *


class Window_Template:
    def __init__(self):
        self.root = Tk()
        self.root.title("Window Template")
        self.root.geometry("500x500")
        self.label = Label(self.root, text="This is the first page").pack()

        

class start(Window_Template):
    def __init__(self):
        super().__init__()
        self.root.title("page 1")
        self.but = Button(self.root, text="click or else", command=self.new_window).pack()

        self.root.mainloop()

    def new_window(self):
        Window_2()
        self.root.destroy()
        


class Window_2(Window_Template):
    def __init__(self):
        super().__init__()
        


if __name__ == "__main__":
    start()