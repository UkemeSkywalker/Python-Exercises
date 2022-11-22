
#******************** Long Route

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image Viewer")


img1 = ImageTk.PhotoImage(Image.open("images/1.JPG"))
img2 = ImageTk.PhotoImage(Image.open("images/2.JPG"))
img3 = ImageTk.PhotoImage(Image.open("images/3.PNG"))
img4 = ImageTk.PhotoImage(Image.open("images/4.png"))
img_list = [img1, img2, img3, img4]


imgWidget = Label(image=img1)
imgWidget.grid(column=2, row=0, )



def foward(number) :
    global forwardBtn
    global imgWidget
    global backwardBtn

    imgWidget.grid_forget()
    imgWidget = Label(image=img_list[number-1])
    
    forwardBtn = Button(root, text="Forward >>", command=lambda: foward(number+1))
    backwardBtn = Button(root, text="<< Backward ", command=lambda:  backward(number-1))

    if number == 4 :
        forwardBtn = Button(root, text="Forward >>", state="disabled")

    imgWidget.grid(column=2, row=0, )
    forwardBtn.grid(column=3, row=1)
    backwardBtn.grid(column=1, row=1)

    statusBar = Label(text= str(number) +" of " + str(len(img_list))+" Images", bd=1, relief="sunken", anchor=E)
    statusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)


def backward(number) :
    global forwardBtn
    global imgWidget
    global backwardBtn

    imgWidget.grid_forget()
    imgWidget = Label(image=img_list[number-1])
    
    forwardBtn = Button(root, text="Forward >>", command=lambda: foward(number+1))
    backwardBtn = Button(root, text="<< Backward ", command=lambda:  backward(number-1))

    if number == 1 :
        backwardBtn = Button(root, text="Backward <<", state="disabled")

    imgWidget.grid(column=2, row=0, )
    forwardBtn.grid(column=3, row=1)
    backwardBtn.grid(column=1, row=1)

    statusBar = Label(text= str(number) +" of " + str(len(img_list))+" Images", bd=1, relief="sunken", anchor=E)
    statusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)

forwardBtn = Button(root, text="Forward >>", command=lambda:foward(2))
exitBtn = Button(root, text="Exit",width="10", command=root.quit, pady=10)
backwardBtn = Button(root, text="<< Backward", command=backward, state="disabled")
statusBar = Label(text="1 of " + str(len(img_list))+" Images", bd=1, relief="sunken", anchor=E)

statusBar.grid(row=2, column=0, columnspan=3, sticky=W+E)
forwardBtn.grid(column=3, row=1)
exitBtn.grid(column=2, row=1)
backwardBtn.grid(column=1, row=1)


root.mainloop()
