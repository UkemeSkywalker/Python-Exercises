from tkinter import *

def click():
    message = Label(root, text="Welcome to Python").grid(row=1, column=0)

root=Tk()
button = Button(root, text="Click Me", padx=100, fg="#fff", bg="#000", command=click).grid(row=0,column=0)

root.mainloop()
