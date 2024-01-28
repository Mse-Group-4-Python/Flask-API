from app.models.instrument_model import InstrumentModel
from app.repositories.instrument_repository import InstrumentRepository

class InstrumentService:
    def __init__(self, instrument_repository: InstrumentRepository):
        self.instrument_repository = instrument_repository

    def get_all_instruments(self):
        return [InstrumentModel(instrument.id,
                                instrument.instrument_name,
                                instrument.manufacturer_id,
                                instrument.category_id,
                                instrument.description,
                                instrument.color ) for instrument in  self.instrument_repository.get_all()]

    def get_instrument_by_id(self, instrument_id):
        instrument = self.instrument_repository.get_by_id(instrument_id)
        return InstrumentModel(instrument.id,
                                instrument.instrument_name,
                                instrument.manufacturer_id,
                                instrument.category_id,
                                instrument.description,
                                instrument.color) if instrument else None 

    def create_instrument(self, instrument):
        self.instrument_repository.create(instrument)

    def update_instrument(self, instrument):
        self.instrument_repository.update(instrument)

    def delete_instrument(self, instrument):
        self.instrument_repository.delete(instrument)
