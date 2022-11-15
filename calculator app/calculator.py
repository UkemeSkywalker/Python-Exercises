from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __inti__(self, master):
        master.title("Small Calculator")
        master.geometry('357*420+0+0')
        master.config(bg="gray")
        master.resizable("false", "false")
    
        self.equation = StringVar()
        self.entry_value=""
        Entry(width=17, textvariable=self.equation).place(x=0, y=0)

    def show(self, value) :
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value("")
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)


root = Tk()
calculator = Calculator(root)
root.mainloop()
