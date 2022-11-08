from tkinter import *


root = Tk()
root.geometry("250x250")

canvas = Canvas(root, width=200, height=200)
canvas.pack()

img = PhotoImage(master=canvas, file="sudoku_gif.gif")
canvas.create_image(100, 100, image=img)

root.mainloop()