from app.models.instrument_item_model import InstrumentItemModel
from app.repositories.instrument_item_repository import InstrumentItemRepository


class InstrumentItemService:
    def __init__(self, instrument_item_repository: InstrumentItemRepository):
        self.instrument_item_repository = instrument_item_repository

    def get_all_instrument_item(self) -> [InstrumentItemModel]:
        return [InstrumentItemModel(entity.id, entity.instrument_id, entity.serial_number, entity.year_of_purchase,
                                    entity.description, entity.price) for entity in
                self.instrument_item_repository.get_all()]

    def get_instrument_item_by_id(self, instrument_item_id):
        return self.instrument_item_repository.get_by_id(instrument_item_id)

    def create_instrument(self, instrument_item):
        self.instrument_item_repository.create(instrument_item)
