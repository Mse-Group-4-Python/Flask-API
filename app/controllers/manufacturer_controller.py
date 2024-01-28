from flask import jsonify
from app.services.manufacturer_service import ManufacturerService

class ManufacturerController:
    manufacturer_service: ManufacturerService

    def __init__(self, manufacturer_service: ManufacturerService = None):
        self.manufacturer_service = manufacturer_service
    
    def get_all(self):
        try:
            manufactures = self.manufacturer_service.get_all_manufacturers()
            response = [manufacture.serialize() for manufacture in manufactures]
            return jsonify(response), 200
        except Exception as ex:
            return jsonify({
                'error': str(ex)
            }), 500
    

    def get_by_id(self, manufacturer_id):
        try:
            manufacture = self.manufacturer_service.get_manufacturer_by_id(manufacturer_id)
            if manufacture:
                return jsonify(manufacture.serialize()), 200
        except Exception as ex:
            return jsonify({
                'error': str(ex)
            }), 500