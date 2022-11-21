from tkinter import *
from  PIL import ImageTk, Image

root = Tk()
root.title('Create New Window')

def window() :
    global img
    newWindow = Toplevel()
    newWindow.title("Photo")
    img = ImageTk.PhotoImage(Image.open("images/4.png"))
    Label(newWindow, image=img).pack()
    Button(newWindow, text="close", command=newWindow.destroy).pack()

Button(root, text="Show Image", command=window).pack()
root.mainloop()