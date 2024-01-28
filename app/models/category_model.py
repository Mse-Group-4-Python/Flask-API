class InstrumentItemOfCategory:
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
        pass


class CategoryModel:
    category_id: int
    category_name: str
    instrument_items: list[InstrumentItemOfCategory]

    def __init__(
        self,
        category_id: int,
        category_name: str,
        instrument_items: list[InstrumentItemOfCategory] = [],
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.instrument_items = instrument_items

    def serialize(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
            "instrument_items": [
                instrument_item.serialize() for instrument_item in self.instrument_items
            ],
        }
        pass
