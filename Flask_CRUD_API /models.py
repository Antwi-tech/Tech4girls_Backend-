# This file is where the creation of tables in the database goes 
from config import session
from sqlalchemy.orm import declarative_base
from sqlalchemy import  Column, Integer, String

# Create a class, here every class specifies the table name you want to use / create 
Base = declarative_base()

class Laptop(Base):
    __tablename__ = 'laptop'
    name = Column(String(50), nullable = False, unique=True)
    laptop_number = Column(Integer, primary_key = True)
    specifications = Column(String(250), nullable=True)
    
    def __str__(self):
        return f'Laptop name: {self.name} has number: {self.laptop_number} and specifications: {self.specifications}'
    
if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print('Laptop table created successfully')
        
    except Exception as e:
        print(f'An error occurred: {e}')    
            