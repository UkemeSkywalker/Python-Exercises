class Cars :

    # global companies 
    # companies = ["Tesla", "Honda", "Audi", "BMW" ]
    global car_names 
    car_names = ["Corolla", "Model X", "Rouge"]

    def __init__(self, company, car_name) :  
        self.company = company
        self.car_name = car_name
        
        print (car_names.append(car_name))

    def list_all_companies(self) :
        print(self.company)
        print(car_names)
        
            
__hash__ = None


car = Cars("Toyota", "Corolla")

print(car)
# car.list_all_companies()

# car_input = car.add_Car_name("Toyota", "Corolla")
# last_car = car.car_names[-1]




# print("New car "+ last_car+ " added")
# print(car.car_names[-1])
# print(car.company)