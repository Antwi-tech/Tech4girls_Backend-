from device import Device
from models import Laptop
from flask import Blueprint, jsonify, request

laptop_device = Blueprint('laptops', __name__)
device = Device()  # Create an instance of the Device class

"""Add a laptop"""
@laptop_device.route('/laptops', methods=['POST'])
def add_laptop():
    details = request.get_json()
    try:
        
        if not details:
            return jsonify({"error": "No data provided"}), 400  # Handle missing request body
        
        new_laptop = device.insert_laptop_details(
            name=details.get('name'),
            laptop_number=details.get('laptop_number'),
            specifications=details.get('specifications')
        )
        
        return jsonify({
            "laptop": {
                "name": new_laptop.name,
                "laptop_number": new_laptop.laptop_number,
                "specifications": new_laptop.specifications
            },
            "message": "Success: 201 Created with confirmation message."
        }), 201
        
    except Exception as e:
        return jsonify({"Unexpected error": {e}})    
    
    
"""Get all laptops"""   
@laptop_device.route('/laptops', methods=['GET'])
def get_all_laptops():
    new_laptop = device.get_laptop()
    laptop_list = []
    try:
        for laptop in new_laptop:
            laptop_list.append({
                "name": laptop.name,
                "laptop_number": laptop.laptop_number,
                "specifications": laptop.specifications
                
            })   
        return jsonify({"Successfully retrieved all laptops:":laptop_list}), 201
    
    except Exception as e:
        return jsonify({"Unexpected error": {e}})
  
""""Get laptop according to name"""    
@laptop_device.route('/laptops/<string:name>', methods=['GET'])
def get_laptop_name(name):
    try:
        laptop= device.get_laptop_by_name(name)
        if not laptop:
            return jsonify({"message": f"Laptop with name {name} not found"}), 400
            
        return jsonify({
            "message": "Laptop details with name displayed successfully.",
            "laptop":{
            "name": laptop.name,
            "laptop_number": laptop.laptop_number,
            "specification": laptop.specifications,
            }
            }), 200
    except Exception as e:
        return jsonify({"Unexpected error": {e}})
    
"""Get laptop according to number"""
@laptop_device.route('/laptops/<int:laptop_number>', methods=['GET'])
def get_laptop_number(laptop_number):
    try:
        laptop= device.get_laptop_by_number(laptop_number)
        if laptop is None:
            return jsonify({"message":f'Laptop with number {laptop_number} does not exist'}), 400
            
        return jsonify({
            "message": f"Successfully found laptop with number:{laptop_number}.",
            "laptop":{
            "name": laptop.name,
            "laptop_number": laptop.laptop_number,
            "specification": laptop.specifications
            }
            }), 200
    except Exception as e:
        return jsonify({"View Error": {e}})    
    
"""Update function"""  
# @laptop_device.route('/laptops/<int:laptop_number>', methods=['PATCH'])
# def update_laptop(laptop_number):
#     updation = request.get_json()
#     for laptop in laptops:
#         if laptop['laptop_number'] == laptop_number:
#             laptop.update(updation)
#             return jsonify({
#                 "message": "Laptop details updated successfully.",
#                 "laptop": laptop
#             }), 200
#     return jsonify({'error': 'Laptop not found'}), 404
  
  
"""Function to update laptop"""    
@laptop_device.route('/laptops/<int:laptop_number>', methods=['PUT'])
def update_laptop(laptop_number):
    try:
        # This stores the new values
        updation = request.get_json()
        # This retrieves all the data vlaues in the database by using the get_laptop_by_number in the device.py
        laptop = device.get_laptop_by_number(laptop_number)
        
        # This updates the laptop you have chosen by number with the values you have chosen
        if laptop:
            if 'name' in updation:
                laptop.name = updation['name']
            if 'specifications' in updation:
                laptop.specifications = updation['specifications']
            
            #After update, it returns the json vlaues if successful 
            return jsonify({
                "message": "Lpatop updated successfully" ,
                "laptop": {
                    "name": laptop.name,
                    "laptop_number": laptop.laptop_number,
                    "specifications": laptop.specifications
                }
            }), 200
            
            # If there is an error that has occured then thsi part runs
        else:
            return jsonify({'Error':'Laptop does not exist.'}), 404
        
    except  Exception as e:
        return jsonify({"Unexpected error": {e}})
            
        
"""Delte a laptop by number"""
@laptop_device.route('/laptops/<int:laptop_number>', methods =['DELETE'])
def delete_laptop(laptop_number):
    try:
        # This gets the particular laptop with number to delete
        laptop = device.get_laptop_by_number(laptop_number)
        
        if not laptop:
            return jsonify({"Error: Laptop Not Found."}), 404 
        
        device.remove_device(laptop_number)
        return jsonify({"message":f'Laptop with {laptop_number} has been deleted'}), 200
        
    except Exception as e:
        return jsonify({'Unexpected error':{e}})
             
       
