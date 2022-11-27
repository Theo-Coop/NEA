from tkinter import *


# root window
root = Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Slider Demo')


slider_val = DoubleVar()


def slider_changed(event):
    text = slider_val.get() / 1000
    current_val_label.config(text=f"Current value: {text}")


slider = Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed, variable=slider_val)
slider.pack()


current_val_label = Label(root, text="Current value: ")
current_val_label.pack()


root.mainloop()