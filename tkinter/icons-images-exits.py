from tkinter import Tk, Button


root = Tk()
root.title("Icons, images & exits")
root.iconbitmap('c:/Users/hp/Dev/Hello Python/images/')

button = Button(root, text="Exit Program", command= root.quit)
button.pack()

root.mainloop()
