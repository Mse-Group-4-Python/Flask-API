from app.models.instrument_item_model import InstrumentItemModel
from app.repositories.instrument_item_repository import InstrumentItemRepository


class InstrumentItemService:
    def __init__(self, instrument_item_repository: InstrumentItemRepository):
        self.instrument_item_repository = instrument_item_repository

    def get_all_instrument_item(self, **kwargs) -> [InstrumentItemModel]:
        return [
            InstrumentItemModel(
                instrument_item_id=entity.id,
                instrument_id=entity.instrument_id,
                serial_number=entity.serial_number,
                year_of_purchase=entity.year_of_purchase,
                description=entity.description,
                price=entity.price,
                instrument_name=entity.instrument.instrument_name,
                color=entity.instrument.color,
                category_name=entity.instrument.category.category_name,
                manufacturer_name=entity.instrument.manufacturer.manufacturer_name,
            )
            for entity in self.instrument_item_repository.get_all(**kwargs)
        ]

    def get_instrument_item_by_id(self, instrument_item_id):
        return self.instrument_item_repository.get_by_id(instrument_item_id)

    def create_instrument(self, instrument_item):
        self.instrument_item_repository.create(instrument_item)

    def update_instrument_item(self, instrument_item_id, instrument_item):
        self.instrument_item_repository.update(instrument_item_id, instrument_item)

    def delete_instrument_item(self, instrument_item_id):
        self.instrument_item_repository.delete(instrument_item_id)
