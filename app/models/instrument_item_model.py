class InstrumentItemModel:
    instrument_item_id: int
    instrument_id: int
    serial_number: str
    description: str
    year_of_purchase: str
    price: float
    instrument_name: str
    category_name: str
    manufacturer_name: str
    color: str

    def __init__(
        self,
        instrument_item_id: int,
        instrument_id: int,
        serial_number: str,
        description: str,
        year_of_purchase: str,
        price: float,
        color: str,
        instrument_name: str,
        category_name: str,
        manufacturer_name: str,
    ):
        self.instrument_item_id = instrument_item_id
        self.instrument_id = instrument_id
        self.serial_number = serial_number
        self.description = description
        self.year_of_purchase = year_of_purchase
        self.price = price
        self.color = color
        self.instrument_name = instrument_name
        self.category_name = category_name
        self.manufacturer_name = manufacturer_name

    def serialize(self):
        return {
            "id": self.instrument_item_id,
            "instrument_id": self.instrument_id,
            "serial_number": self.serial_number,
            "description": self.description,
            "year_of_purchase": self.year_of_purchase,
            "price": self.price,
            "color": self.color,
            "instrument_name": self.instrument_name,
            "category_name": self.category_name,
            "manufacturer_name": self.manufacturer_name,
        }
        pass
