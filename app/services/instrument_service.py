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
                                instrument.color,
                                instrument.tags) for instrument in  self.instrument_repository.get_all()]
        
    def get_instrument_by_search(self, searchTerm: str):
        instruments = self.instrument_repository.get_all()
        keywords = [keyword.lower() for keyword in searchTerm.split(' ')]
        found_instruments = list()
        for instrument in instruments:
            common_items = set(keywords) & set([ tag.lower() for tag in instrument.tags.split(',')])
            print(common_items)
            if (len(common_items) > 0): 
                found_instruments.append(instrument)
        print(found_instruments)

    def get_instrument_by_id(self, instrument_id):
        instrument = self.instrument_repository.get_by_id(instrument_id)
        return InstrumentModel(instrument.id,
                                instrument.instrument_name,
                                instrument.manufacturer_id,
                                instrument.category_id,
                                instrument.description,
                                instrument.color,
                                instrument.tags) if instrument else None 

    def create_instrument(self, instrument):
        self.instrument_repository.create(instrument)

    def update_instrument(self, instrument):
        self.instrument_repository.update(instrument)

    def delete_instrument(self, instrument):
        self.instrument_repository.delete(instrument)
