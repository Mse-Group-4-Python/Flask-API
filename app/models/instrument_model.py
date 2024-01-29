class InstrumentModel:
    id: int
    instrument_name: str
    manufacturer_id: str
    manufacturer_name: str
    category_id: str
    category_name: str
    description: str
    color: str
    tags: str
    instrument_items: list()

    def __init__(
        self,
        id: int,
        instrument_name: str,
        manufacturer_id: str,
        manufacturer_name: str,
        category_id: int,
        category_name: str,
        description: str,
        color: str,
        tags: str,
        instrument_items: list() = [],
    ):
        self.id = (id,)
        self.instrument_name = instrument_name
        self.manufacturer_id = manufacturer_id
        self.manufacturer_name = manufacturer_name
        self.category_id = category_id
        self.category_name = category_name
        self.description = description
        self.color = color
        self.tags = tags
        self.instrument_items = instrument_items

    def serialize(self):
        return {
            "instrument_name": self.instrument_name,
            "manufacturer_id": self.manufacturer_id,
            "category_id": self.category_id,
            "description": self.description,
            "color": self.color,
            "tags": [tag.strip() for tag in self.tags.split(",")],
            "id": self.id[0],
            "instrument_items": [
                instrument_item.serialize() for instrument_item in self.instrument_items
            ],
            "manufacturer_name": self.manufacturer_name,
            "category_name": self.category_name,
        }


class InstrumentItemOfInstrumentModel:
    instrument_name: str
    instrument_item_id: int
    serial_number: str
    year_of_purchase: str
    description: str
    price: float

    def __init__(
        self,
        instrument_name: str,
        instrument_item_id: int,
        serial_number: str,
        year_of_purchase: str,
        description: str,
        price: float,
    ):
        self.instrument_name = instrument_name
        self.instrument_item_id = instrument_item_id
        self.serial_number = serial_number
        self.year_of_purchase = year_of_purchase
        self.description = description
        self.price = price

    def serialize(self):
        return {
            "instrument_name": self.instrument_name,
            "instrument_item_id": self.instrument_item_id,
            "serial_number": self.serial_number,
            "year_of_purchase": self.year_of_purchase,
            "description": self.description,
            "price": self.price,
        }


class InstrumentWithSuggestionResponse:
    instruments: list()
    suggestion: list()

    def __init__(self, instruments, suggestion):
        self.instruments = instruments
        self.suggestion = suggestion

    def serialize(self):
        return {
            "instruments": [instrument.serialize() for instrument in self.instruments],
            "suggestionKeyword": self.suggestion,
        }
