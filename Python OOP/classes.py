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
        



customer1 = Customer("Jude", "Law")

# some_customers = [  Customer("Mom", "Gold"),
#                     Customer("Dad", "Silver"),
#                     Customer("Emman", "Bronze")]


# Customer.all_customers()
# Customer("James", "Platnum")


# print(some_customers[0] == some_customers[1])
# print(some_customers)

# Check object Ids
# print(id(some_customers[0]), id(some_customers[1]))

# print(customer1.name, customer1.membership_type);
# print(some_customers[0].name)

# some_customers[2].update_customer("Water")

# print(some_customers[2].name, some_customers[2].membership_type)

# print(some_customers[1])

# Customer.show_all_customers(some_customers)


class Read_File :

    def open_file() :
        with open("text.txt", "r") as f :
            lines = f.read()
            print(lines)

    def write_on_file(item1, item2, item3):
        with open("text.txt", "w") as f:
            listing = [item1, item2, item3]
            for list in listing:
                add_item = f.writelines(list+ "\n")
            # print(listing + " Added")


# Read_File.write_on_file("Lukaku", "Ukeme", "China")

# Read_File.open_file()