from tkinter import *


root = Tk()
root.geometry("250x250")

def get_info():
    info = input_one.get()
    print(info)


input_one = Entry(root)
input_one.pack()

submit = Button(root, text="submit", command=get_info)
submit.pack()



root.mainloop()