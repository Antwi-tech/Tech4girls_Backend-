import json
from models import Laptop
from device import Device

class DeviceWithJSON(Device):
    def __init__(self):
        super().__init__()

    def export_to_json(self, file_path='data.json'):
        """Export all laptops from the database to a JSON file."""
        laptops = self.get_laptop()
        data = [
            {
                "name": laptop.name,
                "laptop_number": laptop.laptop_number,
                "specifications": laptop.specifications
            }
            for laptop in laptops
        ]
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data exported to {file_path}")

def import_from_json(self, file_path='data.json'):
    """Import laptops from a JSON file to the database."""
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for entry in data:
                existing_laptop = self.get_laptop_by_number(entry['laptop_number'])
                if existing_laptop:
                    # Update the existing record
                    self.update_device(
                        laptop_number=entry['laptop_number'],
                        name=entry.get('name'),
                        specifications=entry.get('specifications')
                    )
                    print(f"Updated laptop: {entry['laptop_number']}")
                else:
                    # Insert a new record
                    self.insert_laptop_details(
                        name=entry['name'],
                        laptop_number=entry['laptop_number'],
                        specifications=entry.get('specifications')
                    )
                    print(f"Inserted new laptop: {entry['laptop_number']}")
        print(f"Data imported from {file_path}")
    except Exception as e:
        print(f"An error occurred during import: {e}")
