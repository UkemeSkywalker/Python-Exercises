from tkinter import Tk, Entry, Button, Label


root = Tk()

class Widgets :

    global input_entry
    input_entry = Entry(root, width=25, bg="#cdcddc")
    position = input_entry.grid(row=0, column=0)


    def onClick() :
        message = "Hello "+input_entry.get()
        output = Label(root, text=message)
        output.grid(row=2, column=0)

    def new_button(text, color, onClick) :
        button = Button(root, text=text, padx=5, command=onClick, bg=color)
        button.grid(row=1, column=0)


Widgets.new_button("submit","red", Widgets.onClick )


root.mainloop()
