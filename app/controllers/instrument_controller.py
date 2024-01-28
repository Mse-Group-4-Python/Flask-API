import json
from flask import jsonify, request

from app.models.models import Instrument
from app.services.instrument_service import InstrumentService


class InstrumentController:
    def __init__(self, instrument_service: InstrumentService):
        self.instrument_service = instrument_service

    def get_all_instruments(self):
        searchTerm = request.args.get('search')
        if (searchTerm is None):
            instruments = self.instrument_service.get_all_instruments()
            instrument_list = [instrument.serialize() for instrument in instruments]
            return jsonify(instrument_list)
        self.instrument_service.get_instrument_by_search(searchTerm)
        
    def get_instrument_by_id(self, instrument_id):
        instrument = self.instrument_service.get_instrument_by_id(instrument_id)
        if instrument:
            return jsonify(instrument.serialize())
        return jsonify({'error': 'Instrument not found'}), 404

    def create_instrument(self):
        data = request.json
        instrument = Instrument(**data)
        self.instrument_service.create_instrument(instrument)
        return jsonify({'message': 'Instrument created successfully'})

    def update_instrument(self, instrument_id):
        data = request.json
        instrument = self.instrument_service.get_instrument_by_id(instrument_id)
        if instrument:
            for key, value in data.items():
                setattr(instrument, key, value)
            self.instrument_service.update_instrument(instrument)
            return jsonify({'message': 'Instrument updated successfully'})
        return jsonify({'error': 'Instrument not found'}), 404

    def delete_instrument(self, instrument_id):
        instrument = self.instrument_service.get_instrument_by_id(instrument_id)
        if instrument:
            self.instrument_service.delete_instrument(instrument)
            return jsonify({'message': 'Instrument deleted successfully'})
        return jsonify({'error': 'Instrument not found'}), 404
