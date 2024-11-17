# Class called car 

class Car: 
    """Class  called car with instance variables make,model and year"""
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        """Function to display car details"""
        return f'The make of the car: {self.make}\nCar Model: {self.model}\nManufacture year: {self.year}\n'
    
  
#This is an instance named car_1    
car_1 = Car('Toyota','Camry',2020)   

#calling the display_info method using print to output results
print(car_1.display_info()) 