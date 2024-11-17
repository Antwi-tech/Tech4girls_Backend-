# 

class Rectangle:
    """Calculate the length and width of the rectangle"""
    def __init__(self,length, width):
        self.length = length
        self.width = width
       
    def area(self):
        cal_area = self.length * self.width
        return f'The area is {cal_area}'
    
    def perimeter(self):
        cal_area = 2*self.length +  2*self.width
        return f'The perimeter is {cal_area}'
    
    def __str__(self):
        """This is string represention that is used to tell the users what the class is doing"""
        return f'Length:{self.length}, Width: {self.width}\n'
    
    def __eq__(self, value):
        """Comparing if 2 instances created are true"""
        if isinstance(value, Rectangle):
            return self.area() == value.area()
        return False
 
# First instance to demonstrate rectangle 
rectangle1 = Rectangle(34, 56)  
print(rectangle1.area()) 
print(rectangle1.perimeter()) 
print(rectangle1)

# Second instance to demonstrate rectangle    
rectangle2 = Rectangle(6, 56)  
print(rectangle2.area()) 
print(rectangle2.perimeter()) 
print(rectangle2)

#Created an instance so that with the use of __eq__() it will be True
rectangle3 = Rectangle(6, 56)  
print(rectangle2 == rectangle3)
        
       
             