from tkinter import Tk, Entry, END, Button, Label


root = Tk()
root.title('Email Slicer')


# Submit Button
def submit() : 
    value = entry.get()        

    (username, domain) = value.split('@')
    (domain , extension) = domain.split('.')

    result = Label(root, text="Username: " + username + " Domain: " + domain + " Extension: " + extension )
    result.grid(row=3, column=0)


#Initialize Widget
home = Label(root, text="Enter Email Address")
entry = Entry(root, width=50 )
submit_Button = Button(root, text="Submit", padx=5, command=submit)


#Display Widget
home.grid(row=0, column=0, pady=10)
entry.grid(row=1, column=0, padx=20,)
submit_Button.grid(row=2, column=0, pady=20)


root.mainloop()