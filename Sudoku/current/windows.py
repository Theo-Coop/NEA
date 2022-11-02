from tkinter import *


class WindowTemplate:
    def __init__(self):
        self.window = Tk()

    def close(self):
        self.window.destroy()