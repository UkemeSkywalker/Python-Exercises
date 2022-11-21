from tkinter import *
from tkinter import filedialog


root = Tk()

root.filename = filedialog.askopenfilename(filetypes=(("All Files", "*.*"), ))
Label(root, text=root.filename).pack()


root.mainloop()