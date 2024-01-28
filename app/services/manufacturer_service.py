from app.models.manufacturer_model import ManufacturerModel
from app.repositories.manufacturer_repository import ManufacturerRepository

class ManufacturerService:
    def __init__(self, manufacturer_repository: ManufacturerRepository) :
        self.manufacturer_repository = manufacturer_repository

    def get_all_manufacturers(self) -> list[ManufacturerModel]:
        temp = self.manufacturer_repository.get_all()
        print("size: " + str(len(temp)))
        return [ManufacturerModel(manufacturer.id,
                                   manufacturer.manufacturer_name) 
                                   for manufacturer in temp]
    
    def get_manufacturer_by_id(self, manufacturer_id):
        manufacturer = self.manufacturer_repository.get_by_id(manufacturer_id)
        print("Name: " + manufacturer.manufacturer_name)
        return ManufacturerModel(manufacturer.id, 
                                 manufacturer.manufacturer_name) if manufacturer else None