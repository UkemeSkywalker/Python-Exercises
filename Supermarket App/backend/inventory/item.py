class Item :

    def __init__(self,  name, description, image, price, tag) -> None:
        
        id = 0
        while 3 > id :
            
            self.id = id
            self.name = name
            self.description = description
            self.image = image
            self.price = price
            self.tag = tag
            id += 1

    def __str__(self) -> str:
        item = str(self.id) + " "+ self.name+ " " + self.description + " "+ self.image+ " "+ str(self.price)+" "+self.tag
        return str(item)
    __repr__ = __str__

add_item = Item("Fanta", "Orange Drink", "Image", 200, "Drinks")

print(add_item)
