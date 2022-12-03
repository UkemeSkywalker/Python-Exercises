## Create Item || Store Item to CSV FIle
## Read Item || Retrive item from CSV file using its index
## Edit Item || and update item in file using its index
## Delete Item || delete item from storage

from item import Item
from storage import Storage

# create new item
def create_item(name, description, image, price, tag) :
    new_item = [Item(name, description, image, price, tag)]
    #Store Item to CSV FIle
    Storage.write_data(new_item)

create_item("Coca Cola", "Cola Drink", "Image", 250, "Soft Drink")


# read all items
def read_all_items() :
    Storage.read_data()

read_all_items()




