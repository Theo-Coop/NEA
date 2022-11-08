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
        default(None)

        self.window.mainloop()

        

class default(WindowTemplate):
    def __init__(self, info):
        super().__init__()
        self.label = Label(self.window, text="Page 1").pack()

        if info:
            self.label = Label(self.window, text=f"Info: {info}").pack()

        self.but = Button(self.window, text="press for input", command=self.buttonpress).pack()



    def buttonpress(self):
        inputs()
        self.close()



class inputs(WindowTemplate):
    def __init__(self):
        super().__init__()
        self.info = None
        self.but = Button(self.window, text="press for page 1", command=self.buttonpress).pack()


        self.input_one = Entry(self.window)
        self.input_one.pack()

        self.submit = Button(self.window, text="submit", command=self.get_info)
        self.submit.pack()

        self.end = Button(self.window, text="Quit", command=self.quit).pack()


    def get_info(self):
        self.info = self.input_one.get()
        print(self.info)

    def buttonpress(self):
        if self.info:
            default(self.info)
        else:
            default("")

        self.close()

    def quit(self):
        # self.window.quit()
        exit() # Either or




hidden()