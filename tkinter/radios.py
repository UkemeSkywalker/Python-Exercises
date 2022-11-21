from tkinter import *

root = Tk()
root.title("Using Radios")

Label(root, text="Choose Icecream Flavour: ")
Icecream = [
    ("Bannana", "Bannana"),
    ("Vanilla", "Vanilla"),
    ("Strawberry", "Strawberry"),
    ("Chocolate", "Chocolate"),
]


x = StringVar()
x.set(" ")

for flavours, types in Icecream :
    Radiobutton(root, text=flavours, variable=x, value=types).pack(anchor=W)


btn = Button(root, text="Submit", command=lambda:submit(x.get()) )
btn.pack()

close = Button(root, text="Exit", command= root.quit).pack()

def submit(value) :
    choice = Label(root, text=value)
    choice.pack()

root.mainloop()