# This file will contain an insertion method into the databse 

from config import session
from models import Laptop

class Device:
    def __init__(self):
        self.session = session
        
    def insert_laptop_details(self, name, laptop_number,specifications):
        new_device = Laptop(name=name,laptop_number=laptop_number,specifications=specifications)
        self.session.add(new_device)
        self.session.commit()
        
        return new_device
    
    def get_laptop(self):
        return session.query(Laptop).all()
        
    def get_laptop_by_name(self, name):
        return session.query(Laptop).filter_by(name=name).first() 
    
    def get_laptop_by_number(self, laptop_number):
        return session.query(Laptop).filter_by(laptop_number=laptop_number).first()
    
    def update_device(self, laptop_number, name = None, specifications = None):
        select_laptop = self.session.query(Laptop).filter_by(laptop_number=laptop_number).first()
        if select_laptop:
            if name:
                select_laptop.name = name
            if specifications:
                select_laptop.specifications = specifications
        session.commit()  
        return select_laptop 
    
    def remove_device(self, laptop_number):
        selected_laptop = self.session.query(Laptop).filter_by(laptop_number=laptop_number).first()  
        if selected_laptop:
            self.session.delete(selected_laptop)     
        session.commit()
        return selected_laptop    
        
        
device = Device()    
"""Instances of laptop"""
# device1 = device.insert_laptop_details("Lenovo IdeaPad Duet 5 OLED Chromebook",4,"Size 13.3 Processor:2.55 GHz Snapdragon .")
# print(device1);
