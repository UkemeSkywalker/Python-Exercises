from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("USing Message Boxes")


# showwarning, showwarning, showerror, askquestion, askokcancel, askyesno

global res

def showinfo() :
    res = messagebox.showinfo("Purple Hibiscus", "Executing Project Purple Hibiscus")
    result(res)

def showwarning() :
    res = messagebox.showwarning("Purple Hibiscus", "Executing Project Purple Hibiscus")
    result(res)

def showerror() :
    res = messagebox.showerror("Purple Hibiscus", "Executing Project Purple Hibiscus")
    result(res)

def askquestion() :
    res = messagebox.askquestion("Purple Hibiscus", "Executing Project Purple Hibiscus")
    result(res)

def askokcancel() :
    res = messagebox.askokcancel("Purple Hibiscus", "Executing Project Purple Hibiscus")
    result(res)

def askyesno() :
    res = messagebox.askyesno("Purple Hibiscus", "Executing Project Purple Hibiscus")
    result(res)

def result(value) :
    Label(root, text=value).pack()

btn = Button(root, text="showinfo", command=showinfo).pack()
btn = Button(root, text="showwarning", command=showwarning).pack()
btn = Button(root, text="showerror", command=showerror).pack()
btn = Button(root, text="askquestion", command=askquestion).pack()
btn = Button(root, text="askokcancel", command=askokcancel).pack()
btn = Button(root, text="askyesno", command=askyesno).pack()
root.mainloop()