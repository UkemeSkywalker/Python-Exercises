from tkinter import Tk, Button, Entry, Label, END

root = Tk()

root.title("Simple Calculator")

def onClickButton(object) :
    input = e.get()
    e.delete(0, END)
    e.insert(0, str(input) + str(object))

def add():
    current = e.get()
    e.delete(0, END)
    global first_input
    global math
    math = "add"
    first_input = current

def sub():
    current = e.get()
    e.delete(0, END)
    global first_input
    global math
    math = "sub"
    first_input = current

def mul():
    current = e.get()
    e.delete(0, END)
    global first_input
    global math
    math = "mul"
    first_input = current

def div():
    current = e.get()
    e.delete(0, END)
    global first_input
    global math
    math = "div"
    first_input = current



def clear() :
    e.delete(0, END)

def equal() :
    second_input = e.get()
    e.delete(0, END)

    if math == "add" :
        e.insert(0, int(first_input) + int(second_input))
    elif math == "sub" :
        e.insert(0, int(first_input) - int(second_input))
    elif math == "mul" :
        e.insert(0, int(first_input) * int(second_input))
    elif math == "div" :
        e.insert(0, int(first_input) / int(second_input))
    else :
        e.insert(0, "")




e = Entry(root, borderwidth=5,  width= 30, bg="#ccddff")
e.grid(row=0, column=0, columnspan=4, padx=2, pady=5)

def create_button(text, padx, pady, number, row, column):
    new_button = Button(text = text,padx = padx, pady = pady, command = lambda: onClickButton(number))
    print("Button Created")
    new_button.grid(row=row, column=column)

# create_button("10", 20, 15, "10")


button7 = create_button("7", 20, 15, 7, 1, 0)
button8 = create_button("8", 20, 15, 8,1,1 )
button9 = create_button("9", 20, 15, 9, 1, 2)
divButton = Button(text="%", padx=20, pady=15, command=div)


def new_func(onClickButton, add, sub, mul, clear, equal, create_button):
    button4 = create_button("4", 20, 15, 4, 2, 0)
    button5 = create_button("5", 20, 15, 5, 2, 1)
    button6 = create_button("6", 20, 15, 6, 2, 2)
    mulButton = Button(text="x ", padx=20, pady=15, command=mul)

    button3 = create_button("3", 20, 15, 3, 3, 0)
    button2 = create_button("2", 20, 15, 2, 3, 1)
    button1 = create_button("1", 20, 15, 1, 3, 2)
    subButton = Button(text="- ", padx=20, pady=15, command=sub)
    # button0 = Button(text="0", padx=20, pady=15, command=lambda: onClickButton(0))
    button0 = create_button("0", 20, 15, 4, 0, 0)
    clearButton = Button(text="CE", padx=20, pady=15, relief='flat', command= clear)
    equalButton = Button(text="=", padx=20, pady=15, bg="blue", fg="#fff", command=equal)
    plusButton = Button(text="+ ", padx=20, pady=15, command=add)
    return mulButton,subButton,button0,clearButton,equalButton,plusButton

mulButton, subButton, button0, clearButton, equalButton, plusButton = new_func(onClickButton, add, sub, mul, clear, equal, create_button)
divButton.grid(row=1, column=3)
mulButton.grid(row=2, column=3)
subButton.grid(row=3, column=3)

clearButton.grid(row=4, column=1)
equalButton.grid(row=4, column=2)
plusButton.grid(row=4, column=3)



root.mainloop()