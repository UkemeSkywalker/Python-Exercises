class Car :

    def __init__(self, company, model ) -> None:
        self.company = company
        self.model = model
    
    def update_model(self, new_model):
        print("Updating model ...")
        self.model = new_model

    
cars = [Car("Toyota", "Highlander"),
        Car("Tesla", "Model Y")]


# print(cars[0].company, cars[0].model)
# cars[0].update_model("Corolla")
# print(cars[0].company, cars[0].model)



class Footballer:

    def __init__(self, name, club, country) -> None:
        self.name = name
        self.club = club
        self.country = country

        print(name +" Club : " +club+" Country :  "+ country+" created" )


    def change_club(self, new_club):
        self.club = new_club
        print(self.name + " has moved to "+ new_club)

f = [Footballer("Ronaldo", "ManU","Portugal"),
    Footballer("Gerrad", "Liverpool", "England")]

print(f[0].name+" plays for "+f[0].club)
f[0].change_club("Arsenal")



