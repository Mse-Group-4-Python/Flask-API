from app.models.models import InstrumentItem
from app.services.instrument_item_service import InstrumentItemService
from flask import jsonify, request


class InstrumentItemController:
    def __init__(self, instrument_item_services: InstrumentItemService):
        self.instrument_item_services = instrument_item_services

    def get_all_instrument_item(self):
        try:
            instrument_items = self.instrument_item_services.get_all_instrument_item()
            instrument_items_list = [instrument_items.serialize() for instrument_items in instrument_items]
            return jsonify(instrument_items_list), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_instrument_item_by_id(self, instrument_item_id):
        try:
            instrument_item = self.instrument_item_services.get_instrument_item_by_id(instrument_item_id)
            if instrument_item:
                return jsonify(instrument_item.serialize()), 200
            return jsonify({'error': 'Instrument Item not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def create_instrument_item(self):
        try:
            data = request.json
            instrument_item = InstrumentItem(**data)
            self.instrument_item_services.create_instrument(instrument_item)
            return jsonify({'message': 'Instrument Item created successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500