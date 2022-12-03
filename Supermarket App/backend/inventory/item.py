

class Item :

    def __init__(self,  name, description, image, price, tag) -> None:

            self.name = name
            self.description = description
            self.image = image
            self.price = price
            self.tag = tag


    def __str__(self) -> str:
        item = self.name+ " " + self.description + " "+ self.image+ " "+ str(self.price)+" "+self.tag
        return str(item)

    __repr__ = __str__






# item1 = [Item("Hisense Tv", "Television", "Image", 300000, "Electical Appliance")]
# item2 = [Item("Fanta", "Orange Drink", "Image", 200, "Drinks")]
# item3 = [Item("Probook15", "Laptop", "Image", 110, "Computers")]

# items = [Item("Hisense Tv", "Television", "Image", 300000, "Electical Appliance"), 
#         Item("Fanta", "Orange Drink", "Image", 200, "Drinks")
# ]


# # print(item1)

# import csv

# f = open("./local.csv", "a", newline='')
# data = csv.writer(f)
# data.writerow(item2)

# f.close()

