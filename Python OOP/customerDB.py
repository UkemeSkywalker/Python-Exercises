from tkinter import *

class Customer :

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        self.write_to_storage()
   

    def update_customer(self, membership_type):
        print("Updating customer records...")
        self.membership_type = membership_type

    def __str__(self) -> str:
        return self.name +" has a " + self.membership_type + "en membership"

    

    def __eq__(self, __o: object) -> bool:
        if self.name == __o.name and self.membership_type == __o.membership_type :
            return True
        return False

    __repr__ = __str__

    def write_to_storage(self):
        with open('data.txt', 'a') as w :
            data = self.name + " "  +self.membership_type
            w.write(str(data)+"\n")
            print("Added to DB")
            

    def all_customers():
        with open("text.txt", "r") as f:
            items = f.read()
            print(items)
        



# customer1 = Customer("Jude", "Law")


## Design User Interface

root = Tk()


def main_widget(root):
    root.title("Create Customer")

    title,name_label, name_e,membership_label, membership_e , submit_btn = create_widget()
    
    Display(title, name_label, name_e, membership_label, membership_e, submit_btn)


def create_widget( ):
    title = Label(root, text="Customer Database", font=('Arial Bold', 30))
    name_label = Label(root, text="Customer Name: ")
    membership_label = Label(root, text="Membership Type: ")
    name_e = Entry(root, width=50 )
    membership_e = Entry(root, width=50 )
    submit_btn = Button(root, text="Submit", width=20,  command=lambda: submit(name_e,membership_e ))   
    print(membership_e.get(), "Line 64")

    return title, name_label, name_e, membership_label, membership_e , submit_btn 


def Display(title, name_label, name_e, membership_label, membership_e, submit_btn ):
    title.pack()
    name_label.pack()
    name_e.pack(pady=10)

    membership_label.pack()
    membership_e.pack(pady=10)

    submit_btn.pack(padx=5, pady=10)


def submit(name, membership):
    name_data = name.get()
    membership_data = membership.get()
    Customer(name_data, membership_data)
    print(name_data, membership_data)
    success_message(name_data)


def success_message(name):
    
    message = Label(root, text="New Customer "+name+" Added")
    message.pack()

main_widget(root)


root.mainloop()