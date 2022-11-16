from tkinter import Tk, Entry, Button, Label


root = Tk()

input = Entry(root, width=25, bg="#cdcddc")
input.grid(row=0, column=0)

def onClick() :
    message = "Hello "+input.get()
    output = Label(root, text=message)
    output.grid(row=2, column=0)

button = Button(root, text="Enter Your Name", padx=5, command=onClick, bg="#cdf")
button.grid(row=1, column=0)


root.mainloop()
