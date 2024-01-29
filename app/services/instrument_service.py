from app.models.instrument_model import (
    InstrumentModel,
    InstrumentWithSuggestionResponse,
    InstrumentItemOfInstrumentModel,
)
from app.repositories.instrument_repository import InstrumentRepository


class InstrumentService:
    def __init__(self, instrument_repository: InstrumentRepository):
        self.instrument_repository = instrument_repository

    def get_all_instruments(self):
        return [
            InstrumentModel(
                instrument_name=instrument.instrument_name,
                category_id=instrument.category_id,
                manufacturer_id=instrument.manufacturer_id,
                description=instrument.description,
                color=instrument.color,
                tags=instrument.tags,
                id=instrument.id,
                category_name=instrument.category.category_name,
                instrument_items=[
                    InstrumentItemOfInstrumentModel(
                        instrument_item_id=instrument_item.id,
                        serial_number=instrument_item.serial_number,
                        year_of_purchase=instrument_item.year_of_purchase,
                        description=instrument_item.description,
                        price=instrument_item.price,
                        instrument_name=instrument_item.instrument.instrument_name,
                    )
                    for instrument_item in instrument.instrument_items
                ],
                manufacturer_name=instrument.manufacturer.manufacturer_name,
            )
            for instrument in self.instrument_repository.get_all()
        ]

    def get_instrument_by_search(self, searchTerm: str):
        instruments = self.instrument_repository.get_all()
        keywords = [keyword.lower() for keyword in searchTerm.split()]
        suggest_keywords = list()
        found_instruments = list()
        for instrument in instruments:
            instrumentTags = list([tag.strip() for tag in instrument.tags.split(",")])
            for tag in instrumentTags:
                for keyword in keywords:
                    if keyword in tag.lower():
                        if tag not in suggest_keywords:
                            suggest_keywords.append(tag)
                        if instrument not in found_instruments:
                            found_instruments.append(instrument)
                    if keyword in instrument.instrument_name.lower():
                        if instrument not in found_instruments:
                            found_instruments.append(instrument)
                    # sort the list by number of matched keywords
        found_instruments.sort(
            key=lambda x: len(
                [
                    keyword
                    for keyword in keywords
                    if keyword in x.tags.lower() or keyword in x.instrument_name.lower()
                ]
            ),
            reverse=True,
        )
        response = InstrumentWithSuggestionResponse(
            [
                InstrumentModel(
                    id=instrument.id,
                    instrument_name=instrument.instrument_name,
                    manufacturer_id=instrument.manufacturer_id,
                    category_id=instrument.category_id,
                    description=instrument.description,
                    color=instrument.color,
                    tags=instrument.tags,
                    category_name=instrument.category.category_name,
                    manufacturer_name=instrument.manufacturer.manufacturer_name,
                    instrument_items=[
                        InstrumentItemOfInstrumentModel(
                            instrument_item_id=instrument_item.id,
                            serial_number=instrument_item.serial_number,
                            year_of_purchase=instrument_item.year_of_purchase,
                            description=instrument_item.description,
                            price=instrument_item.price,
                            instrument_name=instrument_item.instrument.instrument_name,
                        )
                        for instrument_item in instrument.instrument_items
                    ],
                )
                for instrument in found_instruments
            ],
            suggest_keywords,
        )
        return response

    def get_instrument_by_id(self, instrument_id):
        instrument = self.instrument_repository.get_by_id(instrument_id)
        return (
            InstrumentModel(
                instrument.id,
                instrument.instrument_name,
                instrument.manufacturer_id,
                instrument.manufacturer.manufacturer_name,
                instrument.category_id,
                instrument.category.category_name,
                instrument.description,
                instrument.color,
                instrument.tags,
            )
            if instrument
            else None
        )

    def create_instrument(self, instrument):
        self.instrument_repository.create(instrument)

    def update_instrument(self, instrument):
        self.instrument_repository.update(instrument)

    def delete_instrument(self, instrument):
        self.instrument_repository.delete(instrument)
