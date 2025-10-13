""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        print(f" brand :{self.brand} ")
        print(f" model :{self.model} ")
        print(f" year :{self.year} ")

class Car(Vehicle) :
    def __init__(self,brand,model,year,Number_door):
        super().__init__(brand,model,year)
        self.number_door = Number_door
    
    def get_info(self):
        print(f" brand :{self.brand} ")
        print(f" model :{self.model} ")
        print(f" year :{self.year} ")
        print(f" Number_doors :{self.number_door} ")
        

mycar = Car("Honda","Civis","2020","4")
mycar.get_info()