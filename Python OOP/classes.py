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
root.title("Create Customer")



root.mainloop()