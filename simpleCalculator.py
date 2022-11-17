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




button7 = Button(text="7", padx=20, pady=15, command=lambda: onClickButton(7))
button8 = Button(text="8", padx=20, pady=15, command=lambda: onClickButton(8))
button9 = Button(text="9", padx=20, pady=15, command=lambda: onClickButton(9))
divButton = Button(text="%", padx=20, pady=15, command=div)

button4 = Button(text="4", padx=20, pady=15, command=lambda: onClickButton(4))
button5 = Button(text="5", padx=20, pady=15, command=lambda: onClickButton(5))
button6 = Button(text="6", padx=20, pady=15, command=lambda: onClickButton(6))
mulButton = Button(text="x ", padx=20, pady=15, command=mul)

button3 = Button(text="3", padx=20, pady=15, command=lambda: onClickButton(3))
button2 = Button(text="2", padx=20, pady=15, command=lambda: onClickButton(2))
button1 = Button(text="1", padx=20, pady=15, command=lambda: onClickButton(1))
subButton = Button(text="- ", padx=20, pady=15, command=sub)

button0 = Button(text="0", padx=20, pady=15, command=lambda: onClickButton(0))
clearButton = Button(text="CE", padx=20, pady=15, relief='flat', command= clear)
equalButton = Button(text="=", padx=20, pady=15, bg="blue", fg="#fff", command=equal)
plusButton = Button(text="+ ", padx=20, pady=15, command=add)



button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
divButton.grid(row=1, column=3)

button6.grid(row=2, column=0)
button5.grid(row=2, column=1)
button4.grid(row=2, column=2)
mulButton.grid(row=2, column=3)

button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)
subButton.grid(row=3, column=3)

button0.grid(row=4, column=0)
clearButton.grid(row=4, column=1)
equalButton.grid(row=4, column=2)
plusButton.grid(row=4, column=3)



root.mainloop()