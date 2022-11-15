from tkinter import *

root=Tk()
message = Label(root, text="Hello Python!")
message2 = Label(root, text="Welcome Onboard")
message3 = Label(root, text="Learn Automation")

message.grid(row=0, column=0)
message2.grid(row=0, column=1)
message3.grid(row=1, column=1)

root.mainloop()