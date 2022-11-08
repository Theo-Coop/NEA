from tkinter import *


class WindowTemplate:
    def __init__(self):
        self.window = Toplevel()
        self.window.geometry("250x250")
        

    def close(self):
        self.window.destroy()


class hidden:
    def __init__(self):
        self.window = Tk()
        self.label = Label(self.window, text="Hidden").pack()
        self.window.withdraw()
        Window1()

        self.window.mainloop()

        

class Window1(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.label = Label(self.window, text="Page 1").pack()

        self.but = Button(self.window, text="press for page 2", command=self.buttonpress).pack()



    def buttonpress(self):
        Window2()
        self.close()



class Window2(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.label = Label(self.window, text="Page 2").pack()

        self.but = Button(self.window, text="press for page 1", command=self.buttonpress).pack()

        self.end = Button(self.window, text="Quit", command=self.quit).pack()


    def buttonpress(self):
        Window1()
        self.close()

    def quit(self):
        # self.window.quit()
        exit() # Either or



hidden()