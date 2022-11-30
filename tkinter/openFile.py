from tkinter import *
from tkinter import filedialog


root = Tk()

def openFile(root):
    root.filename = filedialog.askopenfilename(filetypes=(("All Files", "*.*"), ))
    Label(root, text=root.filename).pack()

openFile(root)
root.mainloop()