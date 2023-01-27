## Create Item || Store Item to CSV FIle
## Read Item || Retrive item from CSV file using its index
## Edit Item || and update item in file using its index
## Delete Item || delete item from storage

from db import Db


db = "set.db"
def add_item(name, description, image, price, tag, category):
    item = (name, description, image, price, tag, category)
    Db.insert_to_table(db, item)


# Db.create_table(db)
add_item("Hp Probook 15", "Hp Laptop", "Preview", 110000, "Laptop", "Electrical & Appliances")

# Db.delete(db, 4)
# Db.return_one_item(db, 2)

# Db.read(db)
# Db.read_one(db, 2)
# Db.read_all_tags(db)
# Db.read_all_categories(db)

# Db.edit_one_item(db, "Fanta", "Fanta pet 50cl", "preview", 350, "Orange Drink", "Drink", 6)
# Db.edit_tag(db,"Laptops and Tablets", "Laptop")
# Db.edit_category(db, "Book", "Books")

