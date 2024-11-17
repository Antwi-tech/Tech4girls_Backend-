# 

class Employee:
    """Parent class with method called get_details to display the Emplyee name and position"""
    def __init__(self,name, position):
        self.name = name
        self.position = position
        
    def get_details(self):
        return f'Employee name: {self.name}\nEmployee position: {self.position}'   
    
Employee1 = Employee('Rhoda-Oduro', 'Software Engineer')    
print(Employee1.get_details())

class Manager(Employee):
    """Class manager with the parent class passed as Employee"""
    def __init__(self, name, position, department):
        super().__init__(name,position)
        self.department = department
        
    def get_details(self):
        return f'{self.name}\'s department is: {self.department}'    
 
 
# The child class is now used to call the methods and attributes that has been written in the parent class        
Employee1 = Manager('Rhoda-Oduro', 'Software Engineer', 'Information Technology')    
print(Employee1.get_details())
        

        
            
