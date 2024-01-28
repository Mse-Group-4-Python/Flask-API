from app.models.instrument_model import InstrumentModel, InstrumentWithSuggestionResponse
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
        suggest_keywords = list()
        found_instruments = list()
        for instrument in instruments:
            instrumentTags = list([tag.strip() for tag in instrument.tags.split(',')])
            for tag in instrumentTags:
                for keyword in keywords:
                    if keyword in tag.lower():
                        if tag not in suggest_keywords:
                            suggest_keywords.append(tag)
                        if instrument not in found_instruments:
                            found_instruments.append(instrument)
        response = InstrumentWithSuggestionResponse([InstrumentModel(instrument.id,
                                instrument.instrument_name,
                                instrument.manufacturer_id,
                                instrument.category_id,
                                instrument.description,
                                instrument.color,
                                instrument.tags) for instrument in  found_instruments], suggest_keywords)
        return response
        

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
