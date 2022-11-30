from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("USing Message Boxes")


# showwarning, showwarning, showerror, askquestion, askokcancel, askyesno


class Warnings :
    global res

    def showinfo() :
        res = messagebox.showinfo("Purple Hibiscus", "Executing Project Purple Hibiscus")
        Label(root, text=res).pack()

    def showwarning() :
        res = messagebox.showwarning("Purple Hibiscus", "Executing Project Purple Hibiscus")
        Label(root, text=res).pack()

    def showerror() :
        res = messagebox.showerror("Purple Hibiscus", "Executing Project Purple Hibiscus")
        Label(root, text=res).pack()

    def askquestion() :
        res = messagebox.askquestion("Purple Hibiscus", "Executing Project Purple Hibiscus")
        Label(root, text=res).pack()

    def askokcancel() :
        res = messagebox.askokcancel("Purple Hibiscus", "Executing Project Purple Hibiscus")
        Label(root, text=res).pack()

    def askyesno() :
        res = messagebox.askyesno("Purple Hibiscus", "Executing Project Purple Hibiscus")
        Label(root, text=res).pack()


    def show_buttons(showinfo, showwarning, showerror,askquestion, askokcancel, askyesno ) :
        command_list = [showinfo, showwarning, showerror,askquestion, askokcancel, askyesno]
        

        i = 0
        while i < len(command_list):  
            Button(root, text=str(command_list[i]), command=command_list[i]).pack()
            i += 1


Warnings.show_buttons(Warnings.showinfo, Warnings.showwarning, Warnings.showerror,Warnings.askquestion, Warnings.askokcancel, Warnings.askyesno)

# btn = Button(root, text="showinfo", command=showinfo).pack()
# btn = Button(root, text="showwarning", command=showwarning).pack()
# btn = Button(root, text="showerror", command=showerror).pack()
# btn = Button(root, text="askquestion", command=askquestion).pack()
# btn = Button(root, text="askokcancel", command=askokcancel).pack()
# btn = Button(root, text="askyesno", command=askyesno).pack()
root.mainloop()